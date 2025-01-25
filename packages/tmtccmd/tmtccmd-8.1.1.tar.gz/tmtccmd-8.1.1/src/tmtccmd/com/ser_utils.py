import json
import logging
from typing import TextIO, Tuple

import serial
import serial.tools.list_ports
from tmtccmd.util.json import (
    check_json_file,
    JsonKeyNames,
    save_to_json_with_prompt,
)


_LOGGER = logging.getLogger(__name__)


def determine_baud_rate(json_cfg_path: str) -> int:
    """Determine baud rate. Tries to read from JSON first. If the baud rate is not contained
    in the config JSON, prompt it from user instead with the option to store value in JSON file.

    :return: Determined baud rate
    """
    baud_rate = 0
    prompt_baud_rate = False
    if not check_json_file(json_cfg_path=json_cfg_path):
        prompt_baud_rate = True

    if not prompt_baud_rate:
        with open(json_cfg_path, "r") as read:
            try:
                load_data = json.load(read)
                baud_rate = load_data[JsonKeyNames.SERIAL_BAUDRATE.value]
            except KeyError:
                prompt_baud_rate = True

    if prompt_baud_rate:
        while True:
            baud_rate = input("Please enter the baudrate for the serial protocol: ")
            if baud_rate.isdigit():
                baud_rate = int(baud_rate)
                break
            else:
                print("Invalid baud rate specified, try again.")
        with open(json_cfg_path, "r+") as json_file:
            json_obj = json.load(fp=json_file)
            if save_to_json_with_prompt(
                key=JsonKeyNames.SERIAL_BAUDRATE.value,
                value=baud_rate,
                json_cfg_path=json_cfg_path,
                json_obj=json_obj,
                name="baudrate",
            ):
                json_file.seek(0)
                json.dump(json_obj, json_file, indent=4)
    return baud_rate


def determine_com_port(json_cfg_path: str) -> str:
    """Determine serial port. Tries to read from JSON first. If the serial port is not contained
    in the config JSON, prompt it from user instead with the option to store value in JSON file.

    :return: Determined serial port
    """
    reconfig_com_port = False
    if not check_json_file(json_cfg_path=json_cfg_path):
        reconfig_com_port = True
    with open(json_cfg_path, "r+") as json_file:
        com_port = __det_com_port_with_json_file(
            json_cfg_path=json_cfg_path,
            json_file=json_file,
            reconfig_com_port=reconfig_com_port,
        )
    return com_port


def __det_com_port_with_json_file(
    json_cfg_path: str, json_file: TextIO, reconfig_com_port: bool
) -> str:
    try_hint = False
    json_obj = json.load(json_file)
    com_port = ""
    if not reconfig_com_port:
        try_hint, com_port = __try_com_port_load(json_obj=json_obj)
    if try_hint:
        reconfig_com_port, com_port = __try_hint_handling(
            json_cfg_path=json_cfg_path,
            reconfig_com_port=reconfig_com_port,
            json_obj=json_obj,
        )

    if reconfig_com_port:
        com_port = prompt_com_port()
        save_to_json_with_prompt(
            key=JsonKeyNames.SERIAL_PORT.value,
            value=com_port,
            name="serial port",
            json_cfg_path=json_cfg_path,
            json_obj=json_obj,
        )
    json_file.seek(0)
    json.dump(json_obj, json_file, indent=4)
    return com_port


def __try_com_port_load(json_obj) -> Tuple[bool, str]:
    try_hint = False
    com_port = ""
    try:
        com_port = json_obj[JsonKeyNames.SERIAL_PORT.value]
        _LOGGER.info(f"Loaded serial port {com_port} from JSON configuration file")
    except KeyError:
        try_hint = True
    return try_hint, com_port


def __try_hint_handling(json_cfg_path: str, reconfig_com_port: bool, json_obj) -> Tuple[bool, str]:
    reconfig_hint = False
    try:
        hint = json_obj[JsonKeyNames.SERIAL_HINT.value]
    except KeyError:
        reconfig_hint, hint = __prompt_hint_handling(json_obj=json_obj)

    com_port_found, com_port = find_com_port_from_hint(hint=hint)
    if com_port_found:
        _LOGGER.info(f"Found {com_port} based on hint {hint}")
        if reconfig_hint:
            if save_to_json_with_prompt(
                key=JsonKeyNames.SERIAL_PORT.value,
                value=com_port,
                name="serial port",
                json_cfg_path=json_cfg_path,
                json_obj=json_obj,
            ):
                reconfig_com_port = False
    else:
        _LOGGER.info("No serial port found based on hint..")
        reconfig_com_port = True
    return reconfig_com_port, com_port


def __prompt_hint_handling(json_obj) -> Tuple[bool, str]:
    reconfig_hint = False
    hint = ""
    ports = serial.tools.list_ports.comports()
    prompt_hint = input(
        "No hint found in config JSON. Do you want to print the list of devices "
        "and then specify a hint based on it? ([Y]/n): "
    )
    if prompt_hint.lower() in ["y", "yes", "1", ""]:
        while True:
            _LOGGER.info("Found serial devices:")
            for port, desc, hwid in sorted(ports):
                print("{}: {} [{}]".format(port, desc, hwid))
            hint = input("Specify hint: ")
            save_to_json = input(
                "Do you want to store the hint to the configuration file (y) or "
                "specify a new one (r)? ([Y]/r): "
            )
            if save_to_json.lower() in ["y", "yes", "1", ""]:
                json_obj[JsonKeyNames.SERIAL_HINT.value] = hint
                reconfig_hint = True
                break
            elif save_to_json in ["r"]:
                continue
    return reconfig_hint, hint


def find_com_port_from_hint(hint: str) -> Tuple[bool, str]:
    """Find a COM port based on a hint string"""
    if hint == "":
        _LOGGER.warning("Invalid hint, is empty..")
        return False, ""
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        if hint in desc:
            return True, port
    return False, ""


def prompt_com_port() -> str:
    while True:
        com_port = input(
            "Configuring serial port. Please enter serial port"
            ' or "h" to display list of serial ports): '
        )
        if com_port == "h":
            ports = serial.tools.list_ports.comports()
            for port, desc, hwid in sorted(ports):
                print("{}: {} [{}]".format(port, desc, hwid))
        else:
            if not check_port_validity(com_port):
                print("Serial port not in list of available serial ports. Try again?" " ([Y]/n)")
                try_again = input()
                if try_again.lower() in ["y", "yes", ""]:
                    continue
                else:
                    break
            else:
                break
    return com_port


def check_port_validity(com_port_to_check: str) -> bool:
    port_list = []
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        port_list.append(port)
    if com_port_to_check not in port_list:
        return False
    return True
