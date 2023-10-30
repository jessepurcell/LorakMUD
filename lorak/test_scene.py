"""
Test scene
"""
from core.scene import BaseScene


class TestScene(BaseScene):
    def __init__(self):
        super().__init__()

    def update(self):
        super().update()
        # print("Test scene updating")

    def render(self):
        super().render()
        # print("Test scene rendering")
