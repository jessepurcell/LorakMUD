"""
gameobject manager
"""
import pygame.sprite

from core.gameobject import GameObject


class GameObjectManager:
    def __init__(self):
        self._entities = pygame.sprite.Group()

    def update(self):
        for gameobject in self._entities:
            gameobject.update()

    def render(self, window):
        for gameobject in self._entities:
            window.blit(gameobject.surf, gameobject.rect)

    def add_gameobject(self, gameobject):
        self._entities.add(gameobject)
        return gameobject

    def remove_gameobject(self, gameobject: GameObject):
        # self._entities.remove(gameobject)
        gameobject.kill()
