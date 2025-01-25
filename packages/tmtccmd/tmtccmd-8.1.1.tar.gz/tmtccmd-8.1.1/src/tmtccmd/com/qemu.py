#!/usr/bin/env python
"""
QEMU_SERIAL Communication Interface to communicate with emulated QEMU_SERIAL hardware via the
UART interface.

It utilizes the the asyncio library.

Requirements:
  Python >= 3.7 (asyncio support)

Instructions:
  Run QEMU_SERIAL (modified for OBSW) via

  qemu-system-arm -M isis-obc -monitor stdio \
      -bios path/to/sourceobsw-at91sam9g20_ek-sdram.bin \
      -qmp unix:/tmp/qemu,server -S

  Then run the telecommand script with -c 2
"""

import asyncio
import logging
import struct
import json
import re
import errno
import sys
import time
from collections import deque
from threading import Thread
from typing import Optional

from tmtccmd.com import ComInterface
from tmtccmd.tmtc import TelemetryListT
from tmtccmd.com.serial_base import SerialCfg, SerialCommunicationType
from dle_encoder import DleEncoder, STX_CHAR, ETX_CHAR, DleErrorCodes

_LOGGER = logging.getLogger(__name__)
SERIAL_FRAME_LENGTH = 256
DLE_FRAME_LENGTH = 1500

# Paths to Unix Domain Sockets used by the emulator
QEMU_ADDR_QMP = "/tmp/qemu"

# Request/response category and command IDs
IOX_CAT_DATA = 0x01
IOX_CAT_FAULT = 0x02

IOX_CID_DATA_IN = 0x01
IOX_CID_DATA_OUT = 0x02

IOX_CID_FAULT_OVRE = 0x01
IOX_CID_FAULT_FRAME = 0x02
IOX_CID_FAULT_PARE = 0x03
IOX_CID_FAULT_TIMEOUT = 0x04


def start_background_loop(loop: asyncio.AbstractEventLoop) -> None:
    asyncio.set_event_loop(loop)
    loop.run_forever()


class QEMUComIF(ComInterface):
    """Specific Communication Interface implementation of the QEMU_SERIAL USART protocol for the
    TMTC software"""

    def __init__(
        self,
        serial_cfg: SerialCfg,
        ser_com_type: SerialCommunicationType = SerialCommunicationType.DLE_ENCODING,
    ):
        self.cfg = serial_cfg
        self.loop = asyncio.get_event_loop()
        self.number_of_packets = 0
        self.data = []
        self.background_loop_thread: Optional[Thread] = None
        self.usart = None
        self.encoder = None
        self.ser_com_type = ser_com_type
        if self.ser_com_type == SerialCommunicationType.DLE_ENCODING:
            self.encoder = DleEncoder()
            self.reception_buffer = None
            # Set to default value.
            self.dle_queue_len = 10
            self.dle_max_frame = 256
            self.dle_timeout = 0.01

    def __del__(self):
        self.close()

    def is_open(self) -> bool:
        return True

    @property
    def id(self) -> str:
        return self.cfg.com_if_id

    def set_fixed_frame_settings(self, serial_frame_size: int):
        self.serial_frame_size = serial_frame_size

    def set_dle_settings(self, dle_queue_len: int, dle_max_frame: int, dle_timeout: float):
        self.dle_queue_len = dle_queue_len
        self.dle_max_frame = dle_max_frame
        self.dle_timeout = dle_timeout

    def initialize(self, _=None):
        """
        Needs to be called by application code once for DLE mode!
        """
        if not self.loop.is_running():
            self.background_loop_thread = Thread(
                target=start_background_loop, args=(self.loop,), daemon=True
            )

    def open(self, _=None) -> None:
        assert self.background_loop_thread is not None
        self.background_loop_thread.start()
        try:
            self.usart = Usart(self.cfg.serial_port)
            asyncio.run_coroutine_threadsafe(self.usart.open(), self.loop).result()
        except NotImplementedError:
            _LOGGER.exception("QEMU_SERIAL Initialization error, file does not exist!")
            sys.exit()
        if self.ser_com_type == SerialCommunicationType.DLE_ENCODING:
            self.reception_buffer = deque(maxlen=self.dle_queue_len)
            asyncio.run_coroutine_threadsafe(self.start_dle_polling(), self.loop)

    def close(self, _=None) -> None:
        if self.loop.is_closed():
            return

        assert self.usart is not None
        self.loop.call_soon_threadsafe(self.usart.close)
        self.loop.call_soon_threadsafe(self.loop.stop)

        while self.loop.is_running():
            time.sleep(0.01)

        self.loop.close()
        self.background_loop_thread.join()

    async def send_data_async(self, data):
        await self.usart.write(data)
        self.usart.inject_timeout_error()

    def send(self, data: bytearray):
        if self.ser_com_type == SerialCommunicationType.DLE_ENCODING:
            assert self.encoder is not None
            data_encoded = self.encoder.encode(data)
        else:
            data_encoded = data
        self.send_data(data_encoded)

    def send_data(self, data: bytearray):
        asyncio.run_coroutine_threadsafe(self.send_data_async(data), self.loop).result()

    def receive(self, _) -> TelemetryListT:
        assert self.usart is not None
        packet_list = []

        if self.ser_com_type == SerialCommunicationType.DLE_ENCODING:
            while self.reception_buffer:
                data = self.reception_buffer.pop()
                dle_retval, decoded_packet, _ = self.encoder.decode(data)
                if dle_retval == DleErrorCodes.OK:
                    packet_list.append(decoded_packet)
                else:
                    _LOGGER.warning("DLE decoder error!")

        else:
            _LOGGER.warning("This communication type was not implemented yet!")
        return packet_list

    def data_available(self, timeout: float = 0, _=0) -> int:
        if self.ser_com_type == SerialCommunicationType.DLE_ENCODING:
            return self.data_available_dle(timeout=timeout)
        return 0

    def data_available_fixed_frame(self, timeout: float = 0) -> int:
        assert self.usart is not None
        elapsed_time = 0
        start_time = time.time()
        sleep_time = timeout / 3.0
        if timeout > 0:
            while elapsed_time < timeout:
                if self.usart.new_data_available():
                    return self.usart.get_data_in_waiting()

                time.sleep(sleep_time)
                elapsed_time = time.time() - start_time
            return 0
        if self.usart.new_data_available():
            return self.usart.get_data_in_waiting()
        return 0

    def data_available_dle(self, timeout: float = 0) -> int:
        elapsed_time = 0
        start_time = time.time()
        sleep_time = timeout / 3.0
        if timeout > 0:
            while elapsed_time < timeout:
                if self.reception_buffer:
                    return len(self.reception_buffer)
                time.sleep(sleep_time)
                elapsed_time = time.time() - start_time
            return 0
        if self.reception_buffer:
            return len(self.reception_buffer)
        return 0

    async def start_dle_polling(self):
        asyncio.create_task(self.poll_dle_packets())

    async def poll_dle_packets(self):
        assert self.usart is not None
        assert self.reception_buffer is not None
        while True:
            rcvd = await self.usart.read_async(1, timeout=None)

            data = bytearray()
            data.append(rcvd[0])

            if data[0] == STX_CHAR:
                data.extend(
                    await self.usart.read_until_async(
                        bytes([ETX_CHAR]), DLE_FRAME_LENGTH, self.cfg.serial_timeout
                    )
                )

                # check for success
                if data[-1] == ETX_CHAR:
                    self.reception_buffer.appendleft(data)
                    continue

            else:  # not a start byte: flush input buffer
                data.extend(self.usart.read(self.usart.get_data_in_waiting()))

            # handle erroneous data
            print(data)
            # It is assumed that all packets are DLE encoded, so throw it away for now.
            _LOGGER.info("Non DLE-Encoded data with length " + str(len(data) + 1) + " found..")


class QmpException(Exception):
    """An exception caused by the QML/QEMU_SERIAL as response to a failed command"""

    def __init__(self, ret, *args, **kwargs):
        Exception.__init__(self, f"QMP error: {ret}")
        self.ret = ret  # the 'return' structure provided by QEMU_SERIAL/QML


class QmpConnection:
    """A connection to a QEMU_SERIAL machine via QMP"""

    def __init__(self, addr=QEMU_ADDR_QMP):
        self.transport = None
        self.addr = addr
        self.dataq = asyncio.Queue()
        self.initq = asyncio.Queue()
        self.proto = None

    def _protocol(self):
        """The underlying transport protocol"""

        if self.proto is None:
            self.proto = QmpProtocol(self)

        return self.proto

    async def _wait_check_return(self):
        """
        Wait for the status return of a command and raise an exception if it
        indicates a failure
        """

        resp = await self.dataq.get()
        if resp["return"]:
            raise QmpException(resp["return"])

    async def open(self):
        """
        Open this connection. Connect to the machine ensure that the
        connection is ready to use after this call.
        """

        loop = asyncio.get_running_loop()
        await loop.create_unix_connection(self._protocol, self.addr)

        # wait for initial capabilities and version
        init = await self.initq.get()
        print(init)

        # negotioate capabilities
        cmd = '{ "execute": "qmp_capabilities" }'
        self.transport.write(bytes(cmd, "utf-8"))
        await self._wait_check_return()

        return self

    def close(self):
        """Close this connection"""

        if self.transport is not None:
            self.transport.close()
            self.transport = None
            self.proto = None

    async def __aenter__(self):
        await self.open()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        self.close()

    async def cont(self):
        """Continue machine execution if it has been paused"""

        cmd = '{ "execute": "cont" }'
        self.transport.write(bytes(cmd, "utf-8"))
        await self._wait_check_return()

    async def stop(self):
        """Stop/pause machine execution"""

        cmd = '{ "execute": "stop" }'
        self.transport.write(bytes(cmd, "utf-8"))
        await self._wait_check_return()

    async def quit(self):
        """
        Quit the emulation. This causes the emulator to (non-gracefully)
        shut down and close.
        """

        cmd = '{ "execute": "quit" }'
        self.transport.write(bytes(cmd, "utf-8"))
        await self._wait_check_return()


class QmpProtocol(asyncio.Protocol):
    """The QMP transport protocoll implementation"""

    def __init__(self, conn):
        self.conn = conn

    def connection_made(self, transport):
        self.conn.transport = transport

    def connection_lost(self, exc):
        self.conn.transport = None
        self.conn.proto = None

    def data_received(self, data):
        data = str(data, "utf-8")
        decoder = json.JSONDecoder()
        nows = re.compile(r"[^\s]")

        pos = 0
        while True:
            match = nows.search(data, pos)
            if not match:
                return

            pos = match.start()
            obj, pos = decoder.raw_decode(data, pos)

            if "return" in obj:
                self.conn.dataq.put_nowait(obj)
            elif "QMP" in obj:
                self.conn.initq.put_nowait(obj)
            elif "event" in obj:
                pass
            else:
                print("qmp:", obj)


class DataFrame:
    """
    Basic protocol unit for communication via the IOX API introduced for
    external device emulation
    """

    def __init__(self, seq, cat, frame_id, data=None):
        self.seq = seq
        self.cat = cat
        self.id = frame_id
        self.data = data

    def bytes(self):
        """Convert this protocol unit to raw bytes"""
        data = self.data if self.data is not None else []
        return bytes([self.seq, self.cat, self.id, len(data)]) + bytes(data)

    def __repr__(self):
        return (
            f"{{ seq: 0x{self.seq:02x}, cat: 0x{self.cat:02x},"
            f" id: 0x{self.id:02x}, data: {self.data} }}"
        )


def parse_dataframes(buf):
    """Parse a variable number of DataFrames from the given byte buffer"""

    while len(buf) >= 4 and len(buf) >= 4 + buf[3]:
        frame = DataFrame(buf[0], buf[1], buf[2], buf[4 : 4 + buf[3]])
        buf = buf[4 + buf[3] :]
        yield buf, frame

    return buf, None


class UsartStatusException(Exception):
    """An exception returned by the USART send command"""

    def __init__(self, errn, *args, **kwargs):
        Exception.__init__(self, f"USART error: {errno.errorcode[errn]}")
        self.errno = errn  # a UNIX error code indicating the reason


class Usart:
    @staticmethod
    async def create_async(addr):
        return Usart(addr)

    """Connection to emulate a USART device for a given QEMU_SERIAL/At91 instance"""

    def __init__(self, addr):
        self.addr = addr
        self.respd = dict()
        self.respc = asyncio.Condition()
        self.dataq = asyncio.Queue()
        self.datab = bytes()
        self.transport = None
        self.proto = None
        self.seq = 0

    def _protocol(self):
        """The underlying transport protocol"""

        if self.proto is None:
            self.proto = UsartProtocol(self)

        return self.proto

    async def open(self):
        """Open this connection"""

        loop = asyncio.get_running_loop()
        await loop.create_unix_connection(self._protocol, self.addr)
        return self

    def close(self):
        """Close this connection"""

        if self.transport is not None:
            self.transport.close()
            self.transport = None
            self.proto = None

    async def __aenter__(self):
        await self.open()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        self.close()

    def _send_new_frame(self, cat, cid, data=None):
        """
        Send a DataFrame with the given parameters and auto-increase the
        sequence counter. Return its sequence number.
        """
        self.seq = (self.seq + 1) & 0x7F

        frame = DataFrame(self.seq, cat, cid, data)
        self.transport.write(frame.bytes())

        return frame.seq

    async def write(self, data):
        """Write data (bytes) to the USART device"""

        seq = self._send_new_frame(IOX_CAT_DATA, IOX_CID_DATA_IN, data)

        async with self.respc:
            while seq not in self.respd.keys():
                await self.respc.wait()

            resp = self.respd[seq]
            del self.respd[seq]

        status = struct.unpack("I", resp.data)[0]
        if status != 0:
            raise UsartStatusException(status)

    async def __read_async(self, n):
        while len(self.datab) < n:
            frame = await self.dataq.get()
            self.datab += frame.data

    async def read_async(self, n, timeout=None):
        """
        Wait for 'n' bytes to be received from the USART.

        This function will return early if the specified timeout (in
        seconds) is exceeded. In this case, only the data received up to
        that point will be returned. If timeout is None, no timeout will be
        set.
        """

        try:
            await asyncio.wait_for(self.__read_async(n), timeout)
        except asyncio.TimeoutError:
            pass  # ignore timeouts, return data received up to now
        finally:
            m = min(len(self.datab), n)
            data, self.datab = self.datab[:m], self.datab[m:]
            return data

    async def __read_until_async(self, expected, n):
        while n is None or len(self.datab) < n:
            frame = await self.dataq.get()
            self.datab += frame.data

            if expected in frame.data:
                return

    async def read_until_async(self, expected, size=None, timeout=None):
        """
        Read data until either the expected byte sequence has been found,
        the specified number of bytes has been received, or the timeout has
        occured.

        This function will return whatever data has been received up until
        the first termination condition has been met. In case size is None,
        there will be no size limit. In case timeout is None, ther will be
        no timeout.
        """
        try:
            await asyncio.wait_for(self.__read_until_async(expected, size), timeout)
        except asyncio.TimeoutError:
            pass  # ignore timeouts, return data received up to now
        finally:
            end = self.datab.find(expected)
            if end == -1:
                end = len(self.datab)
            else:
                end += len(expected)

            n = min(end, size)
            data, self.datab = self.datab[:n], self.datab[n:]
            return data

    def read(self, n):
        """Wait for 'n' bytes to be received from the USART
        timeout in seconds"""

        try:
            while len(self.datab) < n:
                frame = self.dataq.get_nowait()
                self.datab += frame.data
        # todo better solution
        finally:
            data, self.datab = self.datab[:n], self.datab[n:]
            return data

    def new_data_available(self) -> bool:
        return not self.dataq.empty()

    def get_data_in_waiting(self) -> int:
        return self.dataq.qsize()

    def flush(self):
        while True:
            try:
                self.dataq.get_nowait()
            except Exception as error:
                print(error)
                return

    def inject_overrun_error(self):
        """Inject an overrun error (set CSR_OVRE)"""
        self._send_new_frame(IOX_CAT_FAULT, IOX_CID_FAULT_OVRE)

    def inject_frame_error(self):
        """Inject a frame error (set CSR_FRAME)"""
        self._send_new_frame(IOX_CAT_FAULT, IOX_CID_FAULT_FRAME)

    def inject_parity_error(self):
        """Inject a parity error (set CSR_PARE)"""
        self._send_new_frame(IOX_CAT_FAULT, IOX_CID_FAULT_PARE)

    def inject_timeout_error(self):
        """Inject a timeout (set CSR_TIMEOUT)"""
        self._send_new_frame(IOX_CAT_FAULT, IOX_CID_FAULT_TIMEOUT)


class UsartProtocol(asyncio.Protocol):
    """The USART transport protocoll implementation"""

    def __init__(self, conn):
        self.conn = conn
        self.buf = bytes()

    def connection_made(self, transport):
        self.conn.transport = transport

    def connection_lost(self, exc):
        self.conn.transport = None
        self.conn.proto = None

    def data_received(self, data):
        self.buf += data

        for buf, frame in parse_dataframes(self.buf):
            self.buf = buf

            if frame.cat == IOX_CAT_DATA and frame.id == IOX_CID_DATA_OUT:
                # data from CPU/board to device
                self.conn.dataq.put_nowait(frame)
            elif frame.cat == IOX_CAT_DATA and frame.id == IOX_CID_DATA_IN:
                # response for data from device to CPU/board
                loop = asyncio.get_running_loop()
                loop.create_task(self._data_response_received(frame))

    async def _data_response_received(self, frame):
        async with self.conn.respc:
            self.conn.respd[frame.seq] = frame
            self.conn.respc.notify_all()
