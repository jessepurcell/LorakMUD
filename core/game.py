"""
Game class
Handles general game boilerplate
"""
import pygame

from core.scene_manager import SceneManager
from core.scene import BaseScene
from pygame import locals


class Game:
    FRAME_RATE = 60
    _scene_manager = SceneManager()
    _is_running = False

    def __init__(self, window_size):
        self._window = pygame.display.set_mode(window_size)
        pygame.display.set_caption("Lorak")
        self._clock = pygame.time.Clock()

    def run(self, new_scene: BaseScene):
        print("Game starting...")
        print(f"Loading {new_scene}")
        self._scene_manager.change_scene(new_scene)
        self._is_running = True
        while self._is_running:
            for event in pygame.event.get():
                match event.type:
                    case locals.K_ESCAPE:
                        self._is_running = False
                    case locals.QUIT:
                        self._is_running = False

            pressed_keys = pygame.key.get_pressed()

            self.update()
            self._window.fill((0, 0, 0))
            self.render()
            pygame.display.flip()
            self._clock.tick(self.FRAME_RATE)

    def update(self):
        self._scene_manager.update()

    def render(self):
        self._scene_manager.render(self._window)
