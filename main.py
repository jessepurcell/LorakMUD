"""
Main entry point
"""

from core.game import Game
from lorak.test_scene import TestScene


def main():
    game = Game((1280, 720))
    game.run(TestScene())


if __name__ == '__main__':
    main()
