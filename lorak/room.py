"""
Base room class
"""
from entity import Entity


class Room:
    _entities = []

    def __init__(self):
        pass

    def add_entity(self, entity: Entity):
        self._entities.append(entity)

    def remove_entity(self, entity: Entity):
        self._entities.remove(entity)
