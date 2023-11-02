"""Tileset class"""
import pygame.image


class Tileset:
    def __init__(self, filepath, tile_size=(32, 32), tile_scale=1):
        self.filepath = filepath
        self.tile_size = tile_size
        self.tile_scale = tile_scale
        self.image = pygame.image.load(filepath)
        self.rect = self.image.get_rect()
        self.tiles = []
        self.load()

    def load(self):
        width, height = self.rect.size
        tile_width, tile_height = self.tile_size
        for y in range(0, height, tile_height):
            for x in range(0, width, tile_width):
                tile = pygame.Surface(self.tile_size)
                tile.blit(self.image, (0, 0), (x, y, *self.tile_size))
                tile = pygame.transform.scale(tile, (tile_width * self.tile_scale, tile_height * self.tile_scale))
                self.tiles.append(tile)

    def __str__(self):
        return f'{self.__class__.__name__} file:{self.filepath} tile:{self.tile_size}'
