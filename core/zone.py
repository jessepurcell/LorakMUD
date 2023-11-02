"""
Zone class
"""
from core.tile import Tile


class Zone:
    """
    Keeps track of gameobjects and tiles in a zone
    """

    def __init__(self, tileset):
        self.tileset = tileset
        self.gameobjects = []
        self.tiles = []
        self.grid_size = (0, 0)

    def load(self, filename):
        """Load zone from a file"""
        tile_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                    21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                    0, 0, 0, 0, 1, 5, 7, 12, 4, 6,
                    0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.grid_size = (10, 5)
        for tile_id in tile_ids:
            self.tiles.append(Tile(self.tileset, tile_id))

        i = 0
        for y in range(self.grid_size[1]):
            for x in range(self.grid_size[0]):
                self.tiles[i].rect.x = x * 64
                self.tiles[i].rect.y = y * 64
                i += 1

    def save(self, filename):
        """Save zone to a file"""
        pass
