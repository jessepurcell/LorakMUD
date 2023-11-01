"""
Manages scenes
"""
from core.scene import BaseScene


class SceneManager:
    _current_scene: BaseScene = None

    def __init__(self):
        pass

    def update(self):
        self._current_scene.update()

    def render(self, window):
        self._current_scene.render(window)

    def change_scene(self, new_scene):
        if self._current_scene is not None:
            self._current_scene.destroy()
        self._current_scene = new_scene
        self._current_scene.create()
