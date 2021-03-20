# Python program to implement client side of the control-flow
import socket


def create_server(port: int) -> socket:
    """
    Establishes a connection to a server

    :param port: port to be used
    :return: socket with an active connection to the specified server
    """
    server = socket.socket()
    server.bind((socket.gethostname(), port))
    server.listen(0)
    return server


def connect(address: str, port: int) -> socket:
    """
    Establishes a connection to a server

    :param address: server address to connect to
    :param port: port to be used
    :return: socket with an active connection to the specified server
    """
    conn: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((address, port))
    return conn


def send(conn: socket, msg: str, msg_length: int = 4096) -> bool:
    """
    Sends a message through the supplied connection, and returns whether a response is received
    If a response is received it's printed

    :param conn: connection to send the message through
    :param msg: message to be sent
    :param msg_length: length of the message to be sent. Default is 4096
    :return: whether a response has been received and logged to terminal
    """
    conn.send(msg.encode())
    from_server = conn.recv(msg_length).decode()
    if not from_server:
        return False
    if not "ack" == str(from_server):
        print("Received message different from 'ack' as response. Terminating connection. Response was: "
              + str(from_server))
        terminate(conn)
        return False
    return True


def terminate(conn: socket) -> None:
    """
    terminates the connection of a socket

    :param conn: connection to be terminated
    """
    conn.close()


def run_test() -> None:
    """
    executes a test of the connector, connecting to a socket server at 127.0.0.1:8080,
    then takes input in a while(True) loop, which can be broken with input='q'
    each input different from "q" is sent to the server
    """
    client = connect("127.0.0.1", 8080)
    while True:
        inp = input("Input:")
        if inp == 'q':
            break
        send(client, inp)
    terminate(client)


if __name__ == "__main__":
    run_test()
