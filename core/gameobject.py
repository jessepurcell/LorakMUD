"""
Base gameobject class
"""
import pygame.sprite


class GameObject(pygame.sprite.Sprite):
    def __init__(self, image):
        super(GameObject, self).__init__()
        self.surf = pygame.Surface((0, 0))
        self.surf = image.convert()
        self.rect = self.surf.get_rect()

    def update(self):
        """Run on an gameobject every frame"""
        # print("Updating gameobject")
        pass

    def move(self, offset):
        """Move gameobject by given offset"""
        self.rect.x += offset[0]
        self.rect.y += offset[1]

    def set_position(self, position):
        """Set an gameobject position"""
        self.rect.x = position[0]
        self.rect.y = position[1]
