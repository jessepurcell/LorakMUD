"""Player"""
import pygame

from core.gameobject import GameObject


class Player(GameObject):
    """The player class."""
    _movement_speed = 4

    def __init__(self, image):
        super().__init__(image)

    def update(self):
        # print("Updating player")
        inputs = pygame.key.get_pressed()

        if inputs[pygame.K_w]:
            self.move((0, -self._movement_speed))

        if inputs[pygame.K_s]:
            self.move((0, self._movement_speed))

        if inputs[pygame.K_a]:
            self.move((-self._movement_speed, 0))

        if inputs[pygame.K_d]:
            self.move((self._movement_speed, 0))


