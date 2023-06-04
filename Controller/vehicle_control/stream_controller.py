from time import sleep
from typing import Callable


class StreamControllerI(object):
    """
    Interface for abstracting away handling stream-related actions
    """

    def start_stream(self) -> None:
        """
        Initializes the stream, and begins to stream
        """
        pass

    def stop_stream(self) -> None:
        """
        Requests the temporary stop of video streaming. Terminates the connection
        """
        pass


class SimpleStreamController(StreamControllerI):
    """
    Simple implementation, converting 4 Callables to a StreamController implementation
    """

    def __init__(self, initialize: Callable[[], None], terminate: Callable[[], None], serve: Callable[[], None],
                 stop_serve: Callable[[], None]):
        self.initialize = initialize
        self.terminate = terminate
        self.serve = serve
        self.stop_serve = stop_serve

    def start_stream(self) -> None:
        print("SimpleStreamController", "Initializing")
        self.initialize()
        print("SimpleStreamController", "Starting serving")
        self.serve()
        print("SimpleStreamController", "Started")

    def stop_stream(self) -> None:
        print("SimpleStreamController", "Stopping")
        self.stop_serve()
        sleep(1)
        print("SimpleStreamController", "Terminating")
        self.terminate()
        print("SimpleStreamController", "Terminated")
