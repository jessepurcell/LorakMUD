"""
Test scene
"""
from core.scene import BaseScene
from core.gameobject import GameObject
from core.tileset import Tileset


class TestScene(BaseScene):
    def __init__(self):
        super().__init__()
        self.tileset = Tileset("assets/textures/16x16_Jerom_CC-BY-SA-3.0.png", (16, 16), 4)
        self.test_go = GameObject(self.tileset.tiles[0])
        self.add_gameobject(self.test_go)

    def update(self):
        super().update()
        self.test_go.move((0, 1))
        # print("Test scene updating")

    def render(self, window):
        super().render(window)
        # print("Test scene rendering")
