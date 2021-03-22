from .vehicle_controller_interface import VehicleControllerI


class ControllerSimulator(VehicleControllerI):
    """
    Controller implementation with
    """

    def __init__(self):
        self.drive: int = 0
        self.gear: int = 1
        self.throttle: int = 0
        self.direction: int = 5

    def set_drive(self, val: int) -> None:
        if 0 <= val <= 1:
            self.drive = val

    def set_gear(self, val: int) -> None:
        if 1 <= val <= 4:
            self.gear = val

    def set_throttle(self, val: int) -> None:
        if 0 <= val <= 10:
            self.throttle = val

    def set_direction(self, val: int) -> None:
        if 0 <= val <= 10:
            self.direction = val
