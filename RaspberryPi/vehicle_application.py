import argparse
from typing import List, Dict, Callable

from RaspberryPi.cam import CamStreamer, Streamer
from RaspberryPi.server import Server, DictCommandHandler


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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-port", dest="port", default=8080, type=int)

    cam_streamer = CamStreamer()

    commands = {
        "test": printing_parser("test"),
        "DRIVE": printing_parser("DRIVE"),
        "GEAR": printing_parser("GEAR"),
        "THROTTLE": printing_parser("THROTTLE"),
        "DIRECTION": printing_parser("DIRECTION"),
        **compute_streamer_actions(cam_streamer)
    }

    handler = DictCommandHandler(commands)

    args = parser.parse_args()
    server = Server(port=args.port, command_handler=handler)
    server.server_loop()
