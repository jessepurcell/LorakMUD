"""
Load and contain a tileset
"""
import pygame.image


class Tileset:
    def __init__(self, filepath, size=(32, 32), margin=1, spacing=1):
        self.filepath = filepath
        self.size = size
        self.margin = margin
        self.spacing = spacing
        self.image = pygame.image.load(filepath)
        self.rect = self.image.get_rect()
        self.tiles = []
        self.load()

    def load(self):
        """Load tiles from file and stor in array"""
        self.tiles = []
        x0 = y0 = self.margin
        width, height = self.rect.size
        deltaX = self.size[0] + self.spacing
        deltaY = self.size[0] + self.spacing

        for x in range(x0, width, deltaX):
            for y in range(y0, height, deltaY):
                tile = pygame.Surface(self.size)
                tile.blit(self.image, (0, 0), (x, y, *self.size))
                self.tiles.append(tile)

    def __str__(self):
        return f"{self.__class__.__name__} filepath:{self.filepath} tile:{self.size}"
