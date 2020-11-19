from .base import DrawableObject

from constants import tilesize


'''Abstract class for Moving Entities'''
class MovingObject(DrawableObject):
    def __init__(self, game, x, y, sprite, content):
        super().__init__(game)
        self.rect.x = x*tilesize
        self.rect.y = y*tilesize
        self.rect.w, self.rect.h = tilesize, tilesize

        self.matrix_x = x
        self.matrix_y = y

        self.sprite = sprite
        self.content = content

    def move(self, x, y): # x -> (-1:1), y -> (-1;1)
        self.matrix_x += x
        self.matrix_y += y
        self.update_position()

    def process_draw(self):
        self.game.screen.blit(self.sprite, self.rect)
    
    def update_position(self):
        self.rect.x = self.matrix_x*tilesize
        self.rect.y = self.matrix_y*tilesize

