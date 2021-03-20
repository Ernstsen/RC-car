from typing import List

from serial import Serial
from serial.tools.list_ports import comports
from serial.tools.list_ports_common import ListPortInfo

try:
    from RaspberryPi.micro_controller.controller import Controller
except ModuleNotFoundError:
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
        self.ser.write("D".encode("utf-8"))
        self.ser.write(bytes(val))

    def set_gear(self, val: int) -> None:
        self.ser.write("G".encode("utf-8"))
        self.ser.write(bytes(val))

    def set_throttle(self, val: int) -> None:
        self.ser.write("P".encode("utf-8"))
        self.ser.write(str(val).encode("utf-8"))

    def set_direction(self, val: int) -> None:
        self.ser.write("T".encode("utf-8"))
        self.ser.write(str(val).encode("utf-8"))

    def set_lights(self, val: int) -> None:
        """
        Enables light control

        :param val: 1 for on, 0 for off
        """
        self.ser.write("L".encode("utf-8"))
        self.ser.write(str(val).encode("utf-8"))


if __name__ == "__main__":
    controller: VehicleController = VehicleController()

    print("Possible COM ports:")
    for s in controller.get_possible_ports():
        print(s)

    chosen_port = input("Enter name of COM port to be used:")

    controller.initialize(chosen_port)

    while True:
        inp: str = input("Input")
        if inp == "q":
            break
        elif inp == "drive":
            new_val: int = int(input("Input new value (0/1):"))
            controller.set_drive(new_val)
        elif inp == "gear":
            new_val: int = int(input("Input new value 1-4:"))
            controller.set_gear(new_val)
        elif inp == "throttle":
            new_val: int = int(input("Input new value 0-1:"))
            controller.set_throttle(new_val)
        elif inp == "direction":
            new_val: int = int(input("Input new value 0-2:"))
            controller.set_direction(new_val)
        elif inp == "light":
            new_val: int = int(input("Input new value 0-1:"))
            controller.set_lights(new_val)
