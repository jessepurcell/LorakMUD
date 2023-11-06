"""
Test scene
"""
from core.scene import BaseScene
from core.gameobject import GameObject
from core.tileset import Tileset
from core.zone import Zone
from lorak.player import Player


class TestScene(BaseScene):
    def __init__(self):
        super().__init__()
        self.tileset = Tileset("assets/textures/16x16_Jerom_CC-BY-SA-3.0.png", (16, 16), 4)

        # zone test
        self.test_zone = Zone(self.tileset)
        self.test_zone.load("assets/zones/test.zone")
        for go in self.test_zone.tiles:
            self.add_gameobject(go)

        # gameobject test
        self.test_go = GameObject(self.tileset.tiles[0])
        self.add_gameobject(self.test_go)

        # player test
        self.player = Player(self.tileset.tiles[11])
        self.add_gameobject(self.player)

    def update(self):
        super().update()
        self.test_go.move((0, 1))
        # print("Test scene updating")

    def render(self, window):
        super().render(window)
        # print("Test scene rendering")
