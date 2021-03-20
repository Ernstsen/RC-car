import socket
from Controller.communication import server_utilities as server, Configurator
from .controller import Controller


class VehicleController(Controller):
    """
    Controller implementation communicating with the RC vehicle
    """

    def __init__(self, address: str, port: int):
        self.connection: socket = server.connect(address, port)

    def set_drive(self, val: int) -> None:
        server.send(self.connection, "DRIVE;" + str(val))

    def set_gear(self, val: int) -> None:
        server.send(self.connection, "GEAR;" + str(val))

    def set_throttle(self, val: int) -> None:
        server.send(self.connection, "THROTTLE;" + str(val))

    def set_direction(self, val: int) -> None:
        server.send(self.connection, "DIRECTION;" + str(val))

    def set_lights(self, val: int) -> None:
        server.send(self.connection, "LIGHT;" + str(val))

    def start_stream(self) -> None:
        server.send(self.connection, "STREAM-INITIALIZE;" + Configurator.get_local_ip() + ";8000")
        server.send(self.connection, "STREAM-SERVE-FOOTAGE;")
