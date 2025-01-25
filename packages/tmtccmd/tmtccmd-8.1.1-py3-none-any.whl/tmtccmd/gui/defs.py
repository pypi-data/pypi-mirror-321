from dataclasses import dataclass
import enum
import threading
from typing import Any, Optional

from tmtccmd import CcsdsTmtcBackend
from tmtccmd.config import CoreComInterfaces

CONNECT_BTTN_STYLE = (
    "background-color: #1fc600;"
    "border-style: inset;"
    "font: bold;"
    "color: black;"
    "padding: 6px;"
    "border-width: 2px;"
    "border-radius: 6px;"
)


DISCONNECT_BTTN_STYLE = (
    "background-color: orange;"
    "border-style: inset;"
    "font: bold;"
    "color: black;"
    "padding: 6px;"
    "border-width: 2px;"
    "border-radius: 6px;"
)


COMMAND_BUTTON_STYLE = (
    "background-color: #cdeefd;"
    "border-style: inset;"
    "font: bold;"
    "color: black;"
    "padding: 6px;"
    "border-width: 2px;"
    "border-radius: 6px;"
)


class WorkerOperationsCode(enum.IntEnum):
    OPEN_COM_IF = 0
    CLOSE_COM_IF = 1
    ONE_QUEUE_MODE = 2
    LISTEN_FOR_TM = 3
    UPDATE_BACKEND_MODE = 4
    IDLE = 5


class ComIfRefCount:
    def __init__(self):
        self.lock = threading.Lock()
        self.com_if_used = False
        self.user_cnt = 0

    def add_user(self):
        with self.lock:
            self.user_cnt += 1

    def remove_user(self):
        with self.lock:
            if self.user_cnt > 0:
                self.user_cnt -= 1

    def is_used(self):
        with self.lock:
            if self.user_cnt > 0:
                return True
            return False


class LocalArgs:
    def __init__(self, op_code: WorkerOperationsCode, op_code_args: Any = None):
        self.op_code = op_code
        self.op_args = op_code_args


class SharedArgs:
    def __init__(self, backend: CcsdsTmtcBackend):
        self.state_lock = threading.Lock()
        self.com_if_ref_tracker = ComIfRefCount()
        self.tc_lock = threading.Lock()
        self.backend = backend


@dataclass
class FrontendState:
    current_com_if = CoreComInterfaces.UNSPECIFIED.value
    current_cmd_path: Optional[str] = None
    auto_connect_tm_listener = True
    last_com_if = CoreComInterfaces.UNSPECIFIED.value
    current_com_if_key = CoreComInterfaces.UNSPECIFIED.value
    print_tm = False
    print_raw_tm = False
