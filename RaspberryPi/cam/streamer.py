class Streamer(object):
    """
    Interface for streaming
    """

    def initialize_connection(self, address: str, port: int) -> None:
        """
        Initializes connection to the server
        :param address: address to stream to
        :param port: port to access server on
        """
        pass

    def serve_footage(self, time_limit: int = -1) -> None:
        """
        Serves camera footage live

        If no limit is given, streaming can be stopped by calling 'stop_camera_streaming'

        :param time_limit: how many seconds the stream should be served. If <0, stream continues forever
        """
        pass

    def terminate_connection(self) -> None:
        """
        Terminates connection, and closes socket
        """
        pass

    def stop_camera_streaming(self) -> None:
        """
        Requests that the streamer stops streaming the camera feed
        """
        pass
