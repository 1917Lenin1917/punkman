from .base import DrawableObject

'''Abstract class for Moving Entities'''
class MovingObject(DrawableObject):
    def __init__(self, game):
        super().__init__(game)
