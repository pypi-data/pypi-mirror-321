from datetime import timedelta
from typing import Optional
from unittest import TestCase
from unittest.mock import MagicMock

from spacepackets.ecss import PusTelecommand
from tmtccmd import CcsdsTmtcBackend, CcsdsTmListener, TcHandlerBase
from tmtccmd.com.dummy import DummyComIF
from tmtccmd.core import TcMode, TmMode, BackendRequest
from tmtccmd.core.ccsds_backend import NoValidProcedureSet
from tmtccmd.tmtc import (
    TcProcedureBase,
    TcProcedureType,
    ProcedureWrapper,
)
from tmtccmd.tmtc.handler import FeedWrapper, SendCbParams
from tmtccmd.tmtc.procedure import TreeCommandingProcedure
from tmtccmd.tmtc.queue import DefaultPusQueueHelper, QueueWrapper


class TcHandlerMock(TcHandlerBase):
    def __init__(self, apid: int):
        super().__init__()
        self.apid = apid
        self.is_feed_cb_valid = False
        self.feed_cb_call_count = 0
        self.feed_cb_def_proc_count = 0
        self.send_cb_call_count = 0
        self.queue_helper = DefaultPusQueueHelper(
            queue_wrapper=QueueWrapper.empty(),
            tc_sched_timestamp_len=4,
            pus_verificator=None,
            default_pus_apid=None,
            seq_cnt_provider=None,
        )
        self.send_cb_call_args: Optional[SendCbParams] = None
        self.send_cb_cmd_path_arg: Optional[str] = None

    def send_cb(self, send_params: SendCbParams):
        self.send_cb_call_count += 1
        self.send_cb_call_args = send_params

    def queue_finished_cb(self, info: TcProcedureBase):
        pass

    def feed_cb(self, info: ProcedureWrapper, wrapper: FeedWrapper):
        self.queue_helper.queue_wrapper = wrapper.queue_wrapper
        self.feed_cb_call_count += 1
        self.send_cb_cmd_path_arg = None
        self.send_cb_op_code_arg = None
        if info is not None:
            if info.proc_type == TcProcedureType.TREE_COMMANDING:
                self.feed_cb_def_proc_count += 1
                def_info = info.to_tree_commanding_procedure()
                if def_info.cmd_path != "/ping":
                    self.is_feed_cb_valid = False
                self.send_cb_cmd_path_arg = def_info.cmd_path
                if def_info.cmd_path == "/ping":
                    self.queue_helper.add_pus_tc(
                        PusTelecommand(apid=self.apid, service=17, subservice=1)
                    )
                elif def_info.cmd_path == "/event":
                    self.queue_helper.add_pus_tc(
                        PusTelecommand(apid=self.apid, service=17, subservice=1)
                    )
                    self.queue_helper.add_pus_tc(
                        PusTelecommand(apid=self.apid, service=5, subservice=1)
                    )


class TestBackend(TestCase):
    def setUp(self) -> None:
        self.com_if = DummyComIF()
        self.tm_listener = MagicMock(specs=CcsdsTmListener)
        self.apid = 0x06
        self.tc_handler = TcHandlerMock(self.apid)
        self.backend = CcsdsTmtcBackend(
            tc_mode=TcMode.IDLE,
            tm_mode=TmMode.IDLE,
            com_if=self.com_if,
            tm_listener=self.tm_listener,
            tc_handler=self.tc_handler,
        )
        self.assertEqual(self.backend.tm_listener, self.tm_listener)

    def test_idle(self):
        self.assertEqual(self.backend.tm_mode, TmMode.IDLE)
        self.assertEqual(self.backend.tc_mode, TcMode.IDLE)
        self.assertEqual(self.backend.com_if.id, "dummy")
        self.assertEqual(self.backend.com_if_id, "dummy")
        self.assertEqual(self.backend.inter_cmd_delay, timedelta())
        state = self.backend.state
        self.assertEqual(state.tc_mode, TcMode.IDLE)
        self.assertEqual(state.tm_mode, TmMode.IDLE)
        self.assertEqual(state.next_delay, timedelta())
        self.assertEqual(state.request, BackendRequest.NONE)
        self.backend.mode_to_req()
        self.assertEqual(state.request, BackendRequest.DELAY_IDLE)
        self.assertEqual(self.backend.inter_cmd_delay, timedelta())
        self.assertFalse(self.backend.com_if_active())
        self.assertFalse(self.com_if.is_open())

    def test_basic_ops(self):
        self.backend.start()
        self.assertTrue(self.com_if.is_open())
        self.assertTrue(self.backend.com_if_active())

        res = self.backend.periodic_op()
        self.assertEqual(res.request, BackendRequest.DELAY_IDLE)
        self.backend.tm_mode = TmMode.LISTENER
        self.assertEqual(self.backend.tm_mode, TmMode.LISTENER)
        res = self.backend.periodic_op()
        self.tm_listener.operation.assert_called_once()
        self.backend.poll_tm()
        self.assertEqual(self.tm_listener.operation.call_count, 2)
        self.assertEqual(res.request, BackendRequest.DELAY_LISTENER)
        self.backend.tm_mode = TmMode.IDLE
        self.backend.tc_mode = TcMode.ONE_QUEUE
        with self.assertRaises(NoValidProcedureSet):
            self.backend.periodic_op()
        self.backend.current_procedure = TreeCommandingProcedure(cmd_path="/ping")

        res = self.backend.periodic_op()
        # Only one queue entry which is handled immediately
        self.assertEqual(res.request, BackendRequest.TERMINATION_NO_ERROR)
        self.assertEqual(self.tc_handler.feed_cb_def_proc_count, 1)
        self.assertEqual(self.tc_handler.feed_cb_call_count, 1)
        self.assertEqual(self.tc_handler.send_cb_call_count, 1)
        assert self.tc_handler.send_cb_call_args is not None
        self.assertIsNotNone(self.tc_handler.send_cb_call_args.info)
        self.assertIsNotNone(self.tc_handler.send_cb_call_args.entry)
        self.assertEqual(self.tc_handler.send_cb_call_args.com_if, self.com_if)
        cast_wrapper = self.tc_handler.send_cb_call_args.entry
        pus_entry = cast_wrapper.to_pus_tc_entry()
        self.assertEqual(pus_entry.pus_tc, PusTelecommand(apid=self.apid, service=17, subservice=1))
        self.backend.close_com_if()
        self.assertFalse(self.com_if.is_open())

    def test_one_queue_multi_entry_ops(self):
        self.backend.tm_mode = TmMode.IDLE
        self.backend.tc_mode = TcMode.ONE_QUEUE
        self.backend.current_procedure = TreeCommandingProcedure(cmd_path="/event")
        res = self.backend.periodic_op()
        self.assertEqual(res.request, BackendRequest.CALL_NEXT)
        self.assertEqual(self.tc_handler.feed_cb_def_proc_count, 1)
        self.assertEqual(self.tc_handler.feed_cb_call_count, 1)
        self.assertEqual(self.tc_handler.send_cb_call_count, 1)
        self._check_tc_req_recvd(17, 1)
        res = self.backend.periodic_op()
        self.assertEqual(self.tc_handler.feed_cb_def_proc_count, 1)
        self.assertEqual(self.tc_handler.feed_cb_call_count, 1)
        self.assertEqual(self.tc_handler.send_cb_call_count, 2)
        self._check_tc_req_recvd(5, 1)
        self.assertEqual(res.request, BackendRequest.TERMINATION_NO_ERROR)

    def test_multi_queue_ops(self):
        self.backend.tm_mode = TmMode.IDLE
        self.backend.tc_mode = TcMode.MULTI_QUEUE
        self.backend.current_procedure = TreeCommandingProcedure(cmd_path="/ping")
        res = self.backend.periodic_op()
        self.assertEqual(res.request, BackendRequest.CALL_NEXT)
        self.assertEqual(self.backend.request, BackendRequest.CALL_NEXT)
        self.assertEqual(self.backend.tc_mode, TcMode.IDLE)
        self.assertEqual(self.tc_handler.feed_cb_def_proc_count, 1)
        self.assertEqual(self.tc_handler.feed_cb_call_count, 1)
        self.assertEqual(self.tc_handler.send_cb_call_count, 1)
        self._check_tc_req_recvd(17, 1)
        res = self.backend.periodic_op()
        self.assertEqual(self.tc_handler.feed_cb_call_count, 1)
        self.assertEqual(res.request, BackendRequest.DELAY_IDLE)
        self.backend.tc_mode = TcMode.MULTI_QUEUE
        self.backend.current_procedure = TreeCommandingProcedure(cmd_path="/ping")
        res = self.backend.periodic_op()
        self.assertEqual(res.request, BackendRequest.CALL_NEXT)
        self.assertEqual(self.backend.request, BackendRequest.CALL_NEXT)
        self.assertEqual(self.tc_handler.feed_cb_def_proc_count, 2)
        self.assertEqual(self.tc_handler.feed_cb_call_count, 2)

    def test_procedure_handling(self):
        def_proc = TreeCommandingProcedure(cmd_path="/ping")
        self.backend.current_procedure = def_proc
        self.assertEqual(self.backend.current_procedure.proc_type, TcProcedureType.TREE_COMMANDING)
        proc_helper = self.backend.current_procedure
        def_proc = proc_helper.to_tree_commanding_procedure()
        self.assertIsNotNone(def_proc)
        self.assertEqual(def_proc.cmd_path, "/ping")

    def _check_tc_req_recvd(self, service: int, subservice: int):
        self.assertEqual(self.tc_handler.send_cb_call_args.com_if, self.com_if)
        cast_wrapper = self.tc_handler.send_cb_call_args.entry
        pus_entry = cast_wrapper.to_pus_tc_entry()
        self.assertEqual(
            pus_entry.pus_tc,
            PusTelecommand(apid=self.apid, service=service, subservice=subservice),
        )
