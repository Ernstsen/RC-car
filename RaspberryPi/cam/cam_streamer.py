#
import io
import socket
import struct
import time
from threading import Thread

try:
    import picamera
except ModuleNotFoundError:
    print("Failed to import picamera module - cam wont be usable")

from .streamer import Streamer


class CamStreamer(Streamer):
    """
    Utilizes the RPI cam to serve a stream
    """

    def __init__(self):
        self.rpi_socket: socket = None
        self.connection = None
        self.terminate = False
        self.thread = None
        self.time_limit: int = -1

    def initialize_connection(self, address: str, port: int):
        """
        Initializes connection to the server
        """
        print("Initializing connection")
        self.rpi_socket = socket.socket()
        self.rpi_socket.connect((address, port))
        self.connection = self.rpi_socket.makefile('wb')

    def terminate_connection(self):
        """
        Terminates connection, and closes socket
        """
        self.connection.close()
        self.rpi_socket.close()
        self.connection = None
        self.rpi_socket = None

    def serve_footage(self, time_limit: int = -1) -> None:
        """
        Starts serving video footage in separate thread

        :param time_limit: how many seconds the stream should be served. If <0, stream continues forever
        """
        self.time_limit = time_limit
        self.thread = Thread(target=self.serve_footage_loop)
        self.thread.start()

    def serve_footage_loop(self):
        """
        Serves camera footage live

        If no limit is given, streaming can be stopped by calling 'stop_camera_streaming'
        """
        print("Serving footage!")
        self.terminate = False
        # Make a file-like object out of the connection
        with picamera.PiCamera() as camera:
            camera.resolution = (640, 480)
            camera.rotation = 270
            # Start a preview and let the camera warm up for 2 seconds
            camera.start_preview()
            time.sleep(2)
            camera.stop_preview()

            # Note the start time and construct a stream to hold image data
            # temporarily (we could write it directly to connection but in this
            # case we want to find out the size of each capture first to keep
            # our protocol simple)
            start = time.time()
            stream = io.BytesIO()

            for _ in camera.capture_continuous(stream, 'jpeg'):
                elapsed = time.time()
                # Write the length of the capture to the stream and flush to
                # ensure it actually gets sent
                self.connection.write(struct.pack('<L', stream.tell()))
                self.connection.flush()
                # Rewind the stream and send the image data over the wire
                stream.seek(0)
                self.connection.write(stream.read())
                # If we've been capturing for more than time_limit seconds, quit
                if 0 < self.time_limit < time.time() - start or self.terminate:
                    break
                # Reset the stream for the next capture
                stream.seek(0)
                stream.truncate()
                print("Picture took: " + str(elapsed - time.time()))
        # Write a length of zero to the stream to signal we're done
        self.connection.write(struct.pack('<L', 0))
        print("No longer serving footage")

    def stop_camera_streaming(self) -> None:
        """
        Requests that the streamer stops streaming the camera feed
        """
        self.terminate = True
        self.thread.join()
        self.thread = None


if __name__ == "__main__":
    streamer = CamStreamer()
    try:
        streamer.initialize_connection('192.168.0.110', 8000)
        streamer.serve_footage(-1)
    finally:
        streamer.terminate_connection()
