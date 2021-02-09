# Python program to implement client side of the control-flow

def main():
    import socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8080))
    while True:
        inp = input("Input:")
        if inp == 'q':
            break
        client.send(inp.encode())
        from_server = client.recv(4096).decode()
        print(str(from_server))
    client.close()


if __name__ == "__main__":
    main()
