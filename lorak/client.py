"""
Client entry point
"""

import socket
from networking.netcode import *
from networking.packet import *

SERVER = "127.0.0.1"
ADDRESS = (SERVER, PORT)


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDRESS)
    send_message(client, HelloPacket("Test"))
    # send_message(client, DISCONNECT_MESSAGE)


def send_message(client, packet: BasePacket):
    """Send a message to server"""
    print(packet.get_header())
    print(packet.get_message())
    client.send(packet.get_header())
    client.send(packet.get_message())


if __name__ == '__main__':
    main()
