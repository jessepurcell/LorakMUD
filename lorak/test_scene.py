"""
Test scene
"""
from core.scene import BaseScene
from core.entity import Entity
from core.tileset import Tileset


class TestScene(BaseScene):
    def __init__(self):
        super().__init__()
        # self._entity_manager.add_entity(Entity())
        self.tileset = Tileset("assets/textures/16x16_Jerom_CC-BY-SA-3.0.png", (16, 16))

    def update(self):
        super().update()
        # print("Test scene updating")

    def render(self, window):
        super().render(window)
        window.blit(self.tileset.tiles[6], (0, 0))
        window.blit(self.tileset.tiles[7], (128, 0))
        window.blit(self.tileset.tiles[8], (256, 0))
        # print("Test scene rendering")
