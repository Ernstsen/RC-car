import socket

from .vehicle_controller_interface import VehicleControllerI

try:
    from communication import server_utilities as server, Configurator
except ModuleNotFoundError:
    from Controller.communication import server_utilities as server, Configurator


class VehicleController(VehicleControllerI):
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

    def stream_initialize(self) -> None:
        """
        Requests stream initialization
        """
        server.send(self.connection, "STREAM-INITIALIZE;" + Configurator.get_local_ip() + ";8000")

    def stream_start(self) -> None:
        """
        Requests the vehicle starts streaming
        """
        server.send(self.connection, "STREAM-SERVE-FOOTAGE;")

    def stream_stop(self) -> None:
        """
        Requests that the stream stops - but not terminated
        """
        server.send(self.connection, "STREAM-STOP-STREAMING;")

    def stream_terminate(self) -> None:
        """
        Requests that the video stream is terminated
        """
        server.send(self.connection, "STREAM-TERMINATE;")
