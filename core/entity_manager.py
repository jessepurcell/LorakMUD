"""
Entity manager
"""
from entity import Entity


class EntityManager:
    _entities = []

    def __init__(self):
        pass

    def update(self):
        pass

    def render(self):
        pass

    def add_entity(self, entity):
        self._entities.append(entity)

    def remove_entity(self, entity):
        self._entities.remove(entity)
