import enum
import pprint

from deprecated.sphinx import deprecated
from tmtccmd.core.globals_manager import update_global
from tmtccmd.config.defs import (
    CoreModeList,
    CoreComInterfaces,
)
from tmtccmd.config.tmtc import TmtcDefinitionWrapper

DEF_WRAPPER = None


class CoreGlobalIds(enum.IntEnum):
    """
    Numbers from 128 to 200 are reserved for core globals
    """

    # Object handles
    TMTC_HOOK = 128
    COM_INTERFACE_HANDLE = 129
    TM_LISTENER_HANDLE = 130
    TMTC_PRINTER_HANDLE = 131
    TM_HANDLER_HANDLE = 132
    PRETTY_PRINTER = 133

    # Parameters
    JSON_CFG_PATH = 139
    MODE = 141
    CURRENT_SERVICE = 142
    COM_IF = 144
    OP_CODE = 145
    TM_TIMEOUT = 146
    SERVICE_OP_CODE_DICT = 147
    COM_IF_DICT = 148

    # Miscellaneous
    DISPLAY_MODE = 150
    USE_LISTENER_AFTER_OP = 151
    PRINT_HK = 152
    PRINT_TM = 153
    PRINT_RAW_TM = 154
    PRINT_TO_FILE = 155
    RESEND_TC = 156
    TC_SEND_TIMEOUT_FACTOR = 157

    # Config dictionaries
    USE_SERIAL = 160
    SERIAL_CONFIG = 161
    USE_ETHERNET = 162
    ETHERNET_CONFIG = 163
    END = 300


@deprecated(version="6.0.0rc0", reason="globals module deprecated")
def set_default_globals_pre_args_parsing(
    apid: int,
    com_if_id: str = CoreComInterfaces.DUMMY.value,
    custom_com_if_dict=None,
    display_mode="long",
    tm_timeout: float = 4.0,
    print_to_file: bool = True,
    tc_send_timeout_factor: float = 2.0,
):
    if custom_com_if_dict is None:
        custom_com_if_dict = dict()
    update_global(CoreGlobalIds.COM_IF, com_if_id)
    update_global(CoreGlobalIds.TC_SEND_TIMEOUT_FACTOR, tc_send_timeout_factor)
    update_global(CoreGlobalIds.TM_TIMEOUT, tm_timeout)
    update_global(CoreGlobalIds.DISPLAY_MODE, display_mode)
    update_global(CoreGlobalIds.PRINT_TO_FILE, print_to_file)
    update_global(CoreGlobalIds.CURRENT_SERVICE, 17)
    update_global(CoreGlobalIds.SERIAL_CONFIG, dict())
    update_global(CoreGlobalIds.ETHERNET_CONFIG, dict())
    pp = pprint.PrettyPrinter()
    update_global(CoreGlobalIds.PRETTY_PRINTER, pp)
    update_global(CoreGlobalIds.TM_LISTENER_HANDLE, None)
    update_global(CoreGlobalIds.COM_INTERFACE_HANDLE, None)
    update_global(CoreGlobalIds.TMTC_PRINTER_HANDLE, None)
    update_global(CoreGlobalIds.PRINT_RAW_TM, False)
    update_global(CoreGlobalIds.USE_LISTENER_AFTER_OP, True)
    update_global(CoreGlobalIds.RESEND_TC, False)
    update_global(CoreGlobalIds.OP_CODE, "0")
    update_global(CoreGlobalIds.MODE, CoreModeList.LISTENER_MODE)


@deprecated(version="6.0.0rc0", reason="globals module deprecated")
def check_and_set_other_args(args):
    if args.listener is not None:
        update_global(CoreGlobalIds.USE_LISTENER_AFTER_OP, args.listener)
    if args.tm_timeout is not None:
        update_global(CoreGlobalIds.TM_TIMEOUT, args.tm_timeout)
    if args.print_hk is not None:
        update_global(CoreGlobalIds.PRINT_HK, args.print_hk)
    if args.print_tm is not None:
        update_global(CoreGlobalIds.PRINT_TM, args.print_tm)
    if args.raw_print is not None:
        update_global(CoreGlobalIds.PRINT_RAW_TM, args.raw_print)
    if args.print_log is not None:
        update_global(CoreGlobalIds.PRINT_TO_FILE, args.print_log)
    if args.resend_tc is not None:
        update_global(CoreGlobalIds.RESEND_TC, args.resend_tc)
    update_global(CoreGlobalIds.TC_SEND_TIMEOUT_FACTOR, 3)


@deprecated(version="8.0.0", reason="use command tree API instead")
def get_default_tmtc_defs() -> TmtcDefinitionWrapper:
    global DEF_WRAPPER
    if DEF_WRAPPER is None:
        DEF_WRAPPER = TmtcDefinitionWrapper()
    return DEF_WRAPPER
