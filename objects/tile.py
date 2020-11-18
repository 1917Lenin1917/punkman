import pygame
from constants import Content, Color


class Tile:
    tilesize = 30

    def __init__(self, x=0, y=0, cnt=Content.EMPTY):
        # Rect object for hitboxing
        self.rect = pygame.rect.Rect(x*self.tilesize, y*self.tilesize, self.tilesize, self.tilesize)
        # real matrix coordinates
        self.real_x = self.rect.x//self.tilesize
        self.real_y = self.rect.y//self.tilesize
        # what's inside the tile
        self.content = cnt
        self.color = None
        self.__set_color()

    def __str__(self):
        return self.content

    def __set_color(self):
        if   self.content == Content.PACMAN: self.color = Color.YELLOW
        elif self.content == Content.WALL: self.color = Color.BLUE
        elif self.content == Content.CHERRY: self.color = Color.RED
        else: self.color = Color.WHITE
