"""
Test scene
"""
from core.scene import BaseScene
from core.entity import Entity
from core.tilemap import Tilemap
from core.tileset import Tileset


class TestScene(BaseScene):
    def __init__(self):
        super().__init__()
        self._entity_manager.add_entity(Entity())
        self.tileset = Tileset("assets/textures/overworld.png")
        self.tilemap = Tilemap(self.tileset)
        self.tilemap.set_random()
        self.tilemap.render()

    def update(self):
        super().update()
        # print("Test scene updating")

    def render(self, window):
        super().render(window)
        window.blit(self.tilemap.image, self.tilemap.rect)
        # print("Test scene rendering")
