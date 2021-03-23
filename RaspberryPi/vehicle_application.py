import argparse
from typing import List, Dict, Callable

try:
    from RaspberryPi.cam import CamStreamer, Streamer
    from RaspberryPi.server import Server, DictCommandHandler
    from RaspberryPi.micro_controller import VehicleController
except ModuleNotFoundError:
    from cam import CamStreamer, Streamer
    from server import Server, DictCommandHandler
    from micro_controller import VehicleController


def printing_parser(prefix: str):
    return lambda inp: printing_inner(prefix, inp)


def printing_inner(prefix: str, inp: List[str]):
    i: int = 0
    for arg in inp:
        print(prefix + "arg" + str(i) + ": " + arg)
        i += 1


def compute_streamer_actions(streamer: Streamer) -> Dict[str, Callable[[List[str]], None]]:
    """
    Builds map for stream actions, given the streamer object

    :param streamer: streamer to be manipulated through commands
    :return: dictionary for all stream-related commands
    """
    return {
        "STREAM-INITIALIZE": lambda inp: streamer.initialize_connection(inp[0], int(inp[1])),
        "STREAM-SERVE-FOOTAGE": lambda inp: streamer.serve_footage(),
        "STREAM-STOP-STREAMING": lambda inp: streamer.stop_camera_streaming(),
        "STREAM-TERMINATE": lambda inp: streamer.terminate_connection()
    }


def compute_controller_actions(controller: VehicleController) -> Dict[str, Callable[[List[str]], None]]:
    """
    Builds map for vehicle control actions

    :param controller: vehicle controller
    :return: dictionary for all controller-related commands
    """
    return {
        "LIGHT": lambda inp: controller.set_lights(int(inp[0])),
        "DRIVE": lambda inp: controller.set_drive(int(inp[0])),
        "GEAR": lambda inp: controller.set_gear(int(inp[0])),
        "THROTTLE": lambda inp: controller.set_throttle(int(inp[0])),
        "DIRECTION": lambda inp: controller.set_direction(int(inp[0])),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-port", dest="port", default=8080, type=int)

    cam_streamer = CamStreamer()

    vehicle_controller = VehicleController()
    vehicle_controller.initialize("/dev/ttyUSB0")

    commands = {
        **compute_controller_actions(vehicle_controller),
        **compute_streamer_actions(cam_streamer)
    }

    handler = DictCommandHandler(commands)

    args = parser.parse_args()
    server = Server(port=args.port, command_handler=handler)
    server.server_loop()
