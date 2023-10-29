"""
Packet class
"""

HEADER_SIZE = 128


class BasePacket:
    _message = "BasePacket"  # Don't set directly

    def get_packet_size(self):
        return len(self._message)

    def get_header(self):
        # header = str(self._message).encode('utf-8')
        # header += b' ' * (HEADER_SIZE - len(header))
        # return str(len(self._message)).encode('utf-8') + b' ' * HEADER_SIZE

        send_length = str(self.get_packet_size()).encode('utf-8')
        send_length += b' ' * (HEADER_SIZE - len(send_length))
        return send_length

    def get_message(self):
        return self._message.encode('utf-8')

    def set_message(self, message):
        self._message = message


class HelloPacket(BasePacket):
    def __init__(self, message):
        self.set_message(message)


class DisconnectPacket(BasePacket):
    def __init__(self, message):
        self.set_message(message)
