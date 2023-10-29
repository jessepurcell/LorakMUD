"""
Packet class
"""


class BasePacket:
    _message = "BasePacket"

    def __init__(self, message):
        self._message = message

    def __str__(self):
        return "Packet"

    def __repr__(self):
        return self.__str__()

    def get_size(self):
        pass


class DisconnectPacket(BasePacket):
    def __init__(self, message):
        super().__init__(message)
