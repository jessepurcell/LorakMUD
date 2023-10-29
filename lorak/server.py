"""
Server entry point
"""

import socket
import threading

from networking.netcode import *
from networking.packet import *

PORT = 9521
SERVER = "0.0.0.0"
ADDRESS = (SERVER, PORT)


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDRESS)
    server.listen()
    print(f"Server is listening on {SERVER}:{PORT}")
    while True:
        connection, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(connection, address))
        thread.start()
        print(f"Active connections: {threading.active_count() - 1}")  # horrible


def handle_client(connection, address):
    """Handle client messages"""
    print(f"{address} connected")
    is_connected = True
    while is_connected:
        message = connection.recv(HEADER_SIZE).decode('utf-8')
        if len(message) > 0:
            message_length = int(message)
            message = connection.recv(message_length).decode('utf-8')
            print(f"{address} -> [{message_length}]{message}")
    connection.close()


if __name__ == '__main__':
    main()
