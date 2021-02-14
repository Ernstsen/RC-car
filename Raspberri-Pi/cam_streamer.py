#
import io
import socket
import struct
import time

import picamera


class CamStreamer(object):
    """
    Utilizes the RPI cam to serve a stream
    """

    def __init__(self, address: str, port: int):
        """
        Constructor
        :param address: server to send camera feed to
        :param port: port to access the server
        """
        self.rpi_socket: socket = None
        self.connection = None
        self.address: str = address
        self.port: int = port

    def initialize_connection(self):
        """
        Initializes connection to the server
        """
        self.rpi_socket = socket.socket()
        self.rpi_socket.connect((self.address, self.port))
        self.connection = self.rpi_socket.makefile('wb')

    def terminate_connection(self):
        """
        Terminates connection, and closes socket
        """
        self.connection.close()
        self.rpi_socket.close()

    def serve_footage(self, time_limit: int = -1):
        """
        Serves camera footage live

        :param time_limit: how many seconds the stream should be served. If <0, stream continues forever
        """
        # Make a file-like object out of the connection
        with picamera.PiCamera() as camera:
            camera.resolution = (640, 480)
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

            elapsed = 0
            for foo in camera.capture_continuous(stream, 'jpeg'):
                elapsed = time.time()
                # Write the length of the capture to the stream and flush to
                # ensure it actually gets sent
                self.connection.write(struct.pack('<L', stream.tell()))
                self.connection.flush()
                # Rewind the stream and send the image data over the wire
                stream.seek(0)
                self.connection.write(stream.read())
                # If we've been capturing for more than time_limit seconds, quit
                if 0 < time_limit < time.time() - start:
                    break
                # Reset the stream for the next capture
                stream.seek(0)
                stream.truncate()
                print("Picture took: " + str(elapsed - time.time()))
        # Write a length of zero to the stream to signal we're done
        self.connection.write(struct.pack('<L', 0))


if __name__ == "__main__":
    streamer = CamStreamer('192.168.0.110', 8000)
    try:
        streamer.initialize_connection()
        streamer.serve_footage(-1)
    finally:
        streamer.terminate_connection()
