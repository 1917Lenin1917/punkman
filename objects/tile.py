import pygame

from constants import Content

class Tile:
    tilesize = 10
    def __init__(self, x = 0, y = 0, cnt = Content.EMPTY):
        # Rect object for hitboxing
        self.rect = pygame.rect.Rect(x*self.tilesize, y*self.tilesize, self.tilesize, self.tilesize)
        # real matrix coordinates
        self.real_x = self.rect.x//self.tilesize
        self.real_y = self.rect.y//self.tilesize
        # what's inside the tile
        self.content = cnt

    def __str__(self):
        return self.content
