from typing import Callable


class StreamControllerI(object):
    """
    Interface for abstracting away handling stream-related actions
    """

    def initialize_connection(self) -> None:
        """
        Initializes the stream
        """
        pass

    def terminate_connection(self) -> None:
        """
        Terminates streaming
        """
        pass

    def serve_footage(self) -> None:
        """
        Begins serving footage, requires an active connection.
        """
        pass

    def stop_camera_streaming(self) -> None:
        """
        Requests the temporary stop of video streaming. Does not terminate the active connection
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

    def initialize_connection(self) -> None:
        self.initialize()

    def terminate_connection(self) -> None:
        self.terminate()

    def serve_footage(self) -> None:
        self.serve()

    def stop_camera_streaming(self) -> None:
        self.stop_serve()
