from threading import Lock
from typing import Optional
import warnings

warnings.warn("the globals_manager module is deprecated", DeprecationWarning, stacklevel=2)

__GLOBALS_DICT = dict()
__LOCK_TIMEOUT = 50
__GLOBALS_LOCK = Lock()


def get_global(global_param_id: int, lock: bool = False):
    global __LOCK_TIMEOUT, __GLOBALS_DICT
    if lock:
        __GLOBALS_LOCK.acquire(timeout=__LOCK_TIMEOUT)
    global_param = __GLOBALS_DICT.get(global_param_id)
    if lock:
        __GLOBALS_LOCK.release()
    return global_param


def update_global(global_param_id: int, parameter: any, lock: bool = False):
    global __LOCK_TIMEOUT, __GLOBALS_DICT
    if lock:
        __GLOBALS_LOCK.acquire(timeout=__LOCK_TIMEOUT)
    __GLOBALS_DICT[global_param_id] = parameter
    if lock:
        __GLOBALS_LOCK.release()


def lock_global_pool(blocking: Optional[bool] = None, timeout: Optional[float] = None) -> bool:
    """Lock the global objects. This is important if the values are changed. Don't forget to unlock
    the pool after finishing work with the globals!
    :param timeout_seconds: Attempt to lock for this many second. Default value -1 blocks
    permanently until lock is released.
    :return: Returns whether lock was locked or not.
    """
    global __LOCK_TIMEOUT, __GLOBALS_LOCK
    if blocking is None:
        blocking = True
    if timeout is None:
        timeout = __LOCK_TIMEOUT
    return __GLOBALS_LOCK.acquire(blocking=blocking, timeout=timeout)


def unlock_global_pool():
    global __GLOBALS_LOCK
    """Releases the lock so other objects can use the global pool as well"""
    return __GLOBALS_LOCK.release()


def set_lock_timeout(timeout: float):
    global __LOCK_TIMEOUT
    """Set the timeout for the globals manager lock which can ensure thread-safety"""
    __LOCK_TIMEOUT = timeout
