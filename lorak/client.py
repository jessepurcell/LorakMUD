"""
Client entry point
"""

import socket

SERVER = "127.0.0.1"
ADDRESS = (SERVER, PORT)


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDRESS)
    send_message(client, "Hello, World!")
    send_message(client, "Hello, A!")
    send_message(client, "Hello, B!")
    send_message(client, DISCONNECT_MESSAGE)


def send_message(client, message):
    """Send a message to server"""
    message = message.encode(FORMAT)
    message_length = len(message)
    send_length = str(message_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


if __name__ == '__main__':
    main()
