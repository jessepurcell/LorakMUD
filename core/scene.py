"""
Base scene class
"""
from core.gameobject_manager import GameObjectManager


class BaseScene:
    def __init__(self):
        self._gameobject_manager = GameObjectManager()

    def __str__(self):
        return f"{type(self)}"

    def create(self):
        pass

    def update(self):
        self._gameobject_manager.update()

    def render(self, window):
        self._gameobject_manager.render(window)

    def destroy(self):
        pass

    def add_gameobject(self, gameobject):
        self._gameobject_manager.add_gameobject(gameobject)
