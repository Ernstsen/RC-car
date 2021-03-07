from typing import List

from serial import Serial
from serial.tools.list_ports import comports
from serial.tools.list_ports_common import ListPortInfo

from .controller import Controller


class VehicleController(Controller):
    """
    Controller implementation communicating with the RC vehicle
    """

    def __init__(self):
        self.ser = None

    @staticmethod
    def get_possible_ports() -> List[str]:
        """
        :return: list of ports available
        """
        ports: List[ListPortInfo] = comports()

        port_strings: List[str] = []
        for a, b, c in sorted(ports):
            port_strings.append(str(b))

        return port_strings

    def initialize(self, port: str) -> None:
        """
        Establishes a connection on the given port

        :param port: the COM-port to be the target of the connection
        """
        self.ser: Serial = Serial(port=port, baudrate=115200, timeout=2)

    def terminate(self) -> None:
        """
        closes the serial connection, if present.
        """
        if self.ser:
            self.ser.close()
            self.ser = None

    def set_drive(self, val: int) -> None:
        self.ser.write("DRIVE".encode("utf-8"))
        self.ser.write(bytes(val))

    def set_gear(self, val: int) -> None:
        self.ser.write("GEAR".encode("utf-8"))
        self.ser.write(bytes(val))

    def set_throttle(self, val: int) -> None:
        self.ser.write("THRTL".encode("utf-8"))
        self.ser.write(bytes(val))

    def set_direction(self, val: int) -> None:
        self.ser.write("DIR__".encode("utf-8"))
        self.ser.write(bytes(val))
