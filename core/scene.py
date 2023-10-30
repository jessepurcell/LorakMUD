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
        pass

    def render(self):
        pass

    def destroy(self):
        pass
