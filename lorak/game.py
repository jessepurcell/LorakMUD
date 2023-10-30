"""
Game class
Handles general game boilerplate
"""


class Game:
    _current_scene = None

    def __init__(self, window_size, window_title, scene):
        self.window_size = window_size
        self.window_title = window_title
        self.change_scene(scene)

    def update(self):
        pass

    def render(self):
        pass

    def change_scene(self, scene):
        pass
