from time import sleep
from serial import Serial
from pydantic import BaseModel
from typing import Any, Optional

from serial.serialutil import SerialException
from pygfdrivers.common.util.logger_manager import LOGGING_MODE, LoggerManager


class SerialDevice:
    def __init__(self, config: BaseModel) -> None:
        self.config = config
        self.log = LoggerManager(self.config.device.device_name, LOGGING_MODE.DEBUG)

        self.serial_config = self.config.connection.serial
        self.com_port = self.serial_config.com_port
        self.baud_rate = self.serial_config.baud_rate

        term_char = self.serial_config.term_char.replace('\\r', '\r')
        self.termination = ord(term_char)

        self.serial = self.connect()

        self.is_connected = False
        self.is_configured = False

    def connect(self) -> Optional[Serial]:
        try:
            serial_conn = Serial(self.com_port, self.baud_rate, timeout=1)
            self.is_connected = True
            return serial_conn
        except SerialException as e:
            print(f"Connecting to COM port {self.com_port} encountered error: {e}")
            return None

    def disconnect(self) -> None:
        if self.is_connected and self.serial is not None:
            self.serial.close()

    def check_connection(self) -> None:
        pass

    def write(self, command: int, *args: Any) -> bytes:
        cmd = [command] + [arg for arg in args if args] + [self.termination]
        self.serial.write(bytes(cmd))

        sleep(2)
        ret = self.serial.read()
        return ret

    def query(self, command: int, *args: Any) -> bytes:
        cmd = [command] + [arg for arg in args if args] + [self.termination]
        self.serial.write(bytes(cmd))

        sleep(1)
        ret = self.serial.read_all()
        return ret
