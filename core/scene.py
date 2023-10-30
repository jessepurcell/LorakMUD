"""
Base scene class
"""


class BaseScene:
    def __init__(self):
        pass

    def __str__(self):
        return f"{type(self)}"

    def create(self):
        pass

    def update(self):
        pass

    def render(self):
        pass

    def destroy(self):
        pass
