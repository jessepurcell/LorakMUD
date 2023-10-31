"""
Test scene
"""
from core.scene import BaseScene
from core.entity import Entity


class TestScene(BaseScene):
    def __init__(self):
        super().__init__()
        self._entity_manager.add_entity(Entity())

    def update(self):
        super().update()
        # print("Test scene updating")

    def render(self, window):
        super().render(window)
        # print("Test scene rendering")
