import argparse
from typing import List

from RaspberryPi.server import Server, DictCommandHandler


def printing_parser(prefix: str):
    return lambda inp: printing_inner(prefix, inp)


def printing_inner(prefix: str, inp: List[str]):
    i: int = 0
    for arg in inp:
        print(prefix + "arg" + str(i) + ": " + arg)
        i += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-port", dest="port", default=8080, type=int)

    commands = {
        "test": printing_parser("test")
    }

    handler = DictCommandHandler(commands)

    args = parser.parse_args()
    server = Server(port=args.port, command_handler=handler)
    server.server_loop()
