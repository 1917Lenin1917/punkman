from .base import DrawableObject

from constants import tilesize


class MovingObject(DrawableObject):
    def __init__(self, game, x, y, sprite, content, map_ref):
        super().__init__(game)
        # pygame screen pos
        self.rect.x = x*tilesize
        self.rect.y = y*tilesize
        self.rect.w, self.rect.h = tilesize, tilesize
        # real matrix position
        self.real_x = x
        self.real_y = y
        # appearence
        self.sprite = sprite
        self.content = content
        # map reference
        self.map = map_ref

    def update_pos(self):
        self.rect.x = self.real_x * tilesize
        self.rect.y = self.real_y * tilesize

    def process_draw(self):
        self.game.screen.blit(self.sprite, self.rect)

