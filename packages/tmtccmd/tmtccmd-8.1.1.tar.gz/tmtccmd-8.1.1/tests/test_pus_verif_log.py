import logging
import os
from pathlib import Path
from unittest import TestCase

from tmtccmd.logging import add_colorlog_console_logger
from spacepackets.ecss import PusTelecommand
from spacepackets.ecss.pus_1_verification import (
    create_acceptance_success_tm,
    create_start_success_tm,
    create_step_success_tm,
    StepId,
    create_completion_success_tm,
    create_acceptance_failure_tm,
    FailureNotice,
    ErrorCode,
    create_start_failure_tm,
)
from spacepackets.ccsds.time import CdsShortTimestamp
from spacepackets.ecss.pus_verificator import PusVerificator
from tmtccmd.logging.pus import RegularTmtcLogWrapper
from tmtccmd.pus import VerificationWrapper


class TestPusVerifLog(TestCase):
    def setUp(self) -> None:
        self.apid = 0x02
        self.log_file_name = RegularTmtcLogWrapper.get_current_tmtc_file_name()
        self.logger = logging.getLogger(__name__)
        add_colorlog_console_logger(self.logger)

    def test_console_log_success(self):
        wrapper = VerificationWrapper(PusVerificator(), self.logger, None)
        self._test_success(wrapper)

    def test_console_log_success_without_colors(self):
        wrapper = VerificationWrapper(PusVerificator(), self.logger, None)
        wrapper.with_colors = False
        self._test_success(wrapper)

    def _test_success(self, wrapper: VerificationWrapper):
        verificator = wrapper.verificator
        tc = PusTelecommand(apid=self.apid, service=17, subservice=1, seq_count=0)
        verificator.add_tc(tc)
        srv_1_tm = create_acceptance_success_tm(
            apid=self.apid, pus_tc=tc, timestamp=CdsShortTimestamp.empty().pack()
        )
        empty_stamp = CdsShortTimestamp.empty().pack()

        def generic_checks():
            self.assertTrue("acc" in cm.output[0])
            self.assertTrue("fin" in cm.output[0])
            self.assertTrue("sta" in cm.output[0])
            self.assertTrue("ste" in cm.output[0])

        res = verificator.add_tm(srv_1_tm)
        with self.assertLogs(self.logger) as cm:
            wrapper.log_to_console(srv_1_tm, res)
            self.assertTrue(
                f"{'Acceptance success of TC'.ljust(25)} | "
                f"Request ID {srv_1_tm.tc_req_id.as_u32():#08x}" in cm.output[0]
            )
            generic_checks()
        srv_1_tm = create_start_success_tm(apid=self.apid, pus_tc=tc, timestamp=empty_stamp)
        res = verificator.add_tm(srv_1_tm)
        with self.assertLogs(self.logger) as cm:
            wrapper.log_to_console(srv_1_tm, res)
            self.assertTrue(
                f"{'Start success of TC'.ljust(25)} | "
                f"Request ID {srv_1_tm.tc_req_id.as_u32():#08x}" in cm.output[0]
            )
            generic_checks()
        srv_1_tm = create_step_success_tm(
            apid=self.apid,
            pus_tc=tc,
            step_id=StepId.with_byte_size(1, 1),
            timestamp=empty_stamp,
        )
        res = verificator.add_tm(srv_1_tm)
        with self.assertLogs(self.logger) as cm:
            wrapper.log_to_console(srv_1_tm, res)
            self.assertTrue(
                f"{'Step success of TC'.ljust(25)} | "
                f"Request ID {srv_1_tm.tc_req_id.as_u32():#08x}" in cm.output[0]
            )
            generic_checks()
        srv_1_tm = create_completion_success_tm(apid=self.apid, pus_tc=tc, timestamp=empty_stamp)
        res = verificator.add_tm(srv_1_tm)
        with self.assertLogs(self.logger) as cm:
            wrapper.log_to_console(srv_1_tm, res)
            self.assertTrue(
                f"{'Completion success of TC'.ljust(25)} | "
                f"Request ID {srv_1_tm.tc_req_id.as_u32():#08x}" in cm.output[0]
            )
            generic_checks()

    def test_console_log_acc_failure(self):
        wrapper = VerificationWrapper(PusVerificator(), self.logger, None)
        self._test_acc_failure(wrapper)

    def test_console_log_acc_failure_without_colors(self):
        wrapper = VerificationWrapper(PusVerificator(), self.logger, None)
        wrapper.with_colors = False
        self._test_acc_failure(wrapper)

    def _test_acc_failure(self, wrapper: VerificationWrapper):
        verificator = wrapper.verificator
        tc = PusTelecommand(apid=self.apid, service=17, subservice=1, seq_count=1)
        verificator.add_tc(tc)
        srv_1_tm = create_acceptance_failure_tm(
            apid=self.apid,
            pus_tc=tc,
            failure_notice=FailureNotice(code=ErrorCode(pfc=8, val=1), data=bytes()),
            timestamp=CdsShortTimestamp.empty().pack(),
        )
        res = verificator.add_tm(srv_1_tm)
        # TODO: Use self.assertLogs here instead
        wrapper.log_to_console(srv_1_tm, res)

    def test_console_log_start_failure(self):
        wrapper = VerificationWrapper(PusVerificator(), self.logger, None)
        verificator = wrapper.verificator
        tc = PusTelecommand(apid=self.apid, service=17, subservice=1, seq_count=2)
        verificator.add_tc(tc)
        srv_1_tm = create_acceptance_failure_tm(
            apid=self.apid,
            pus_tc=tc,
            failure_notice=FailureNotice(code=ErrorCode(pfc=8, val=1), data=bytes()),
            timestamp=CdsShortTimestamp.empty().pack(),
        )
        res = verificator.add_tm(srv_1_tm)
        # TODO: Use self.assertLogs here instead
        wrapper.log_to_console(srv_1_tm, res)
        srv_1_tm = create_start_failure_tm(
            apid=self.apid,
            pus_tc=tc,
            failure_notice=FailureNotice(code=ErrorCode(pfc=8, val=1), data=bytes()),
            timestamp=CdsShortTimestamp.empty().pack(),
        )
        res = verificator.add_tm(srv_1_tm)
        # TODO: Use self.assertLogs here instead
        wrapper.log_to_console(srv_1_tm, res)

    def test_file_logger(self):
        tmtc_logger = RegularTmtcLogWrapper(file_name=self.log_file_name)
        wrapper = VerificationWrapper(PusVerificator(), None, tmtc_logger.logger)
        verificator = wrapper.verificator
        tc = PusTelecommand(apid=self.apid, service=17, subservice=1, seq_count=0)
        verificator.add_tc(tc)
        srv_1_tm = create_acceptance_success_tm(
            apid=self.apid, pus_tc=tc, timestamp=CdsShortTimestamp.empty().pack()
        )
        res = verificator.add_tm(srv_1_tm)
        wrapper.log_to_file(srv_1_tm, res)
        srv_1_tm = create_start_success_tm(
            apid=self.apid, pus_tc=tc, timestamp=CdsShortTimestamp.empty().pack()
        )
        res = verificator.add_tm(srv_1_tm)
        wrapper.log_to_file(srv_1_tm, res)
        srv_1_tm = create_step_success_tm(
            apid=self.apid,
            pus_tc=tc,
            step_id=StepId.with_byte_size(1, 1),
            timestamp=CdsShortTimestamp.empty().pack(),
        )
        res = verificator.add_tm(srv_1_tm)
        wrapper.log_to_file(srv_1_tm, res)
        srv_1_tm = create_completion_success_tm(
            apid=self.apid, pus_tc=tc, timestamp=CdsShortTimestamp.empty().pack()
        )
        res = verificator.add_tm(srv_1_tm)
        wrapper.log_to_file(srv_1_tm, res)
        # Assert that 4 lines have been written
        with open(self.log_file_name) as file:
            all_lines = file.readlines()
            self.assertEqual(len(all_lines), 4)

    def tearDown(self) -> None:
        log_file = Path(self.log_file_name)
        if log_file.exists():
            os.remove(log_file)
