# Python program to implement server of controller software
import argparse
import socket

IP_address = "127.0.0.1"


def main(port: int) -> None:
    family = socket.AF_INET  # address domain of the
    socket_kind = socket.SOCK_STREAM  # data or characters are read in a continuous flow.
    sock = socket.socket(family, socket_kind)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sock.bind(('0.0.0.0', port))
    sock.listen(1)  # listens for only one connection

    while True:
        conn, addr = sock.accept()
        received = ''
        while True:
            data = conn.recv(4096).decode()
            if not data:
                break
            received += data
            print(data)
            conn.send(bytes("Server says: " + received, 'utf-8'))
        conn.close()
        print('client disconnected')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-port", dest="port", default=8080, type=int)

    args = parser.parse_args()
    main(args.port)
