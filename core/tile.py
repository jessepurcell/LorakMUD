"""Tile gameobject"""
from core.gameobject import GameObject


class Tile(GameObject):
    def __init__(self, tilemap, tile_id):
        super().__init__(tilemap.tiles[tile_id])

    def get_world_position(self):
        return self.rect.x, self.rect.y
