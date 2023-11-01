"""
Base entity class
"""
import pygame.sprite


class Entity(pygame.sprite.Sprite):
    def __init__(self):
        super(Entity, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf = pygame.image.load("C:/Dev/LorakMUD/assets/textures/test_tiles.png").convert()
        self.rect = self.surf.get_rect()

    def update(self):
        print("Updating entity")
