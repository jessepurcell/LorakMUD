"""
Base entity class
"""
import pygame.sprite


class Entity(pygame.sprite.Sprite):
    def __init__(self, image):
        super(Entity, self).__init__()
        self.surf = pygame.Surface((0, 0))
        self.surf = image.convert()
        self.rect = self.surf.get_rect()

    def update(self):
        """Run on an entity every frame"""
        print("Updating entity")

    def move(self, offset):
        """Move entity by given offset"""
        self.rect.x += offset[0]
        self.rect.y += offset[1]

    def set_position(self, position):
        """Set an entity position"""
        self.rect.x = position[0]
        self.rect.y = position[1]
