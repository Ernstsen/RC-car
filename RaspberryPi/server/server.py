# Python program to implement server of controller software
import argparse
import socket
import threading

from RaspberryPi.cam import Streamer
from RaspberryPi.server.command_handler import CommandHandler
from RaspberryPi.server.printing_command_handler import PrintingCommandHandler


class Server(object):
    """
    Hosts server as an interface for the RC vehicle
    """

    def __init__(self, port: int = 8080,
                 command_handler: CommandHandler = PrintingCommandHandler(),
                 streamer: Streamer = Streamer()):
        """
        :param port: port to host the server one
        """
        self.port = port
        self.socket = None
        self.streamer = streamer
        self.command_handler = command_handler
        self.stream_thread = None
        self.initialize_server()

    def initialize_server(self) -> None:
        """
        Initializes and configures the server
        """
        family = socket.AF_INET  # address domain of the
        socket_kind = socket.SOCK_STREAM  # data or characters are read in a continuous flow.
        self.socket = socket.socket(family, socket_kind)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.socket.bind(('0.0.0.0', self.port))
        self.socket.listen(1)  # listens for only one connection

    def server_loop(self) -> None:
        """
        The loop listening on the socket, and handling incoming messages
        """
        while True:
            conn, addr = self.socket.accept()
            while True:
                data = conn.recv(4096).decode()
                if not data:
                    break
                self.command_handler.handle_command(data)
                conn.send("ack".encode("UTF-8"))
            conn.close()
            print('client disconnected')

    def start_video_stream(self, target_server_address: str, target_server_port: int) -> None:
        """
        Non-blocking call.
        Starts the camera, and streams the feed to the target server
        :param target_server_address: address for the server to send cam-feed to on the form 'x.x.x.x'
        :param target_server_port:port to access the target server
        """
        self.streamer.initialize_connection(target_server_address, target_server_port)
        self.stream_thread = threading.Thread(target=self.streamer.serve_footage)

    def end_video_stream(self) -> None:
        """
        Stops stream the camera-feed
        """
        if self.streamer:
            self.streamer.stop_camera_streaming()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-port", dest="port", default=8080, type=int)

    args = parser.parse_args()
    server = Server(port=args.port)
    server.server_loop()
