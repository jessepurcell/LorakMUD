"""
Entity manager
"""
import pygame.sprite

from core.entity import Entity


class EntityManager:
    def __init__(self):
        self._entities = pygame.sprite.Group()

    def update(self):
        pass

    def render(self):
        for entity in self._entities:
            entity.blit(entity.surf, entity.rect)

    def add_entity(self, entity: Entity):
        self._entities.add(entity)

    def remove_entity(self, entity: Entity):
        # self._entities.remove(entity)
        entity.kill()
