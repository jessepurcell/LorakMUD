"""Player"""
from core.gameobject import GameObject


class Player(GameObject):
    """The player class."""

    def __init__(self, image):
        super().__init__(image)

    def update(self):
        pass
