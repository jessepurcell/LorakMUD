"""
Game class
Handles general game boilerplate
"""
from scene import BaseScene


class Game:
    _current_scene: BaseScene = None

    def __init__(self, window_size, window_title, scene):
        self.window_size = window_size
        self.window_title = window_title
        self.change_scene(scene)

    def update(self):
        pass

    def render(self):
        pass

    def change_scene(self, new_scene: BaseScene):
        if self._current_scene is not None:
            self._current_scene.cleanup()
        self._current_scene = new_scene
        self._current_scene.initialize()
