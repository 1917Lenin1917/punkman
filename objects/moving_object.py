from .base import DrawableObject

from constants import tilesize, Content


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

    '''checks if next step Tile is not a Wall'''
    def is_able_to_move(self, x, y):
        '''дело в том, что в двумерной матрице первая координата - это строка или же Y, а вторая - X'''
        return self.map.tile_arr[self.real_y + y][self.real_x + x].content != Content.WALL

    def update_pos(self):
        self.rect.x = self.real_x * tilesize
        self.rect.y = self.real_y * tilesize

    def process_draw(self):
        self.game.screen.blit(self.sprite, self.rect)

