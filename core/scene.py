"""
Base scene class
"""
from core.entity_manager import EntityManager


class BaseScene:
    def __init__(self):
        self._entity_manager = EntityManager()

    def __str__(self):
        return f"{type(self)}"

    def create(self):
        pass

    def update(self):
        self._entity_manager.update()

    def render(self, window):
        self._entity_manager.render(window)

    def destroy(self):
        pass

    def add_entity(self, entity):
        self._entity_manager.add_entity(entity)
