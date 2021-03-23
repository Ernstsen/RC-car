# Python program to implement server of controller software
import argparse
import socket

try:
    from RaspberryPi.cam import Streamer
    from RaspberryPi.server.command_handler import CommandHandler
    from RaspberryPi.server.printing_command_handler import PrintingCommandHandler
except ModuleNotFoundError:
    from cam import Streamer
    from server.command_handler import CommandHandler
    from server.printing_command_handler import PrintingCommandHandler


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

    @staticmethod
    def get_local_ip():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 1))  # connect() for UDP doesn't send packets
        return s.getsockname()[0]

    def initialize_server(self) -> None:
        """
        Initializes and configures the server
        """
        family = socket.AF_INET  # address domain of the
        socket_kind = socket.SOCK_STREAM  # data or characters are read in a continuous flow.
        self.socket = socket.socket(family, socket_kind)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.socket.bind((self.get_local_ip(), self.port))
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
                success: bool = self.command_handler.handle_command(data)
                if success:
                    conn.send("ack".encode("UTF-8"))
                else:
                    conn.send("nack".encode("UTF-8"))
            conn.close()
            print('client disconnected')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-port", dest="port", default=8080, type=int)

    args = parser.parse_args()
    server = Server(port=args.port)
    server.server_loop()
