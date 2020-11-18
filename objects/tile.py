import pygame
from constants import Content

class Tile:
    '''tile object for matrix of pacman map'''
    tilesize = 10

    def __init__(self, x = 0, y = 0, cnt = Content.EMPTY, s = None):
        # Rect object for hitboxing
        self.rect = pygame.rect.Rect(x*self.tilesize, y*self.tilesize, self.tilesize, self.tilesize)
        # real matrix coordinates
        self.real_x = self.rect.x//self.tilesize
        self.real_y = self.rect.y//self.tilesize
        # what's inside the tile
        self.content = cnt
        self.screen = s
        self.set_sprite()

    def set_sprite(self):
        '''sets the sprite basing on content of the tile'''
        if self.content == Content.WALL:
            self.sprite = pygame.image.load('sprites/wall.png')

    def __str__(self):
        return self.content

    def draw(self):
        '''blits tile sprite on the exact coordinates of pygame window'''
        self.screen.blit(self.sprite, self.rect)
