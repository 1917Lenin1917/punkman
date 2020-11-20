from .base import DrawableObject

from constants import tilesize


class MovingObject(DrawableObject):
    def __init__(self, game, x, y, sprite, content, speed):
        super().__init__(game)
        self.rect.x = x*tilesize
        self.rect.y = y*tilesize
        self.rect.w, self.rect.h = tilesize, tilesize
        self.speed = speed
        self.shift_y = 0
        self.shift_x = 0

        self.matrix_x = x
        self.matrix_y = y

        self.sprite = sprite
        self.content = content

    def move(self):
        pass

    def process_draw(self):
        self.game.screen.blit(self.sprite, self.rect)

