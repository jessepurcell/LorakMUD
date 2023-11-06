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
        # Will need to update this to store gameobjects?
        tile_ids = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15,
                    15, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 15,
                    15, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 15,
                    15, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 15,
                    15, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 15,
                    15, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 15,
                    15, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 15,
                    15, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 15,
                    15, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 15,
                    15, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 15,
                    15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]

        self.grid_size = (20, 11)
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
