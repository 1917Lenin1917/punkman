import pygame
from constants import Content


class Tile:
    tilesize = 50

    def __init__(self, x, y, cnt, screen):
        # Rect object for hitboxing
        self.rect = pygame.rect.Rect(x*self.tilesize, y*self.tilesize, self.tilesize, self.tilesize)
        # real matrix coordinates
        self.real_x = self.rect.x // self.tilesize
        self.real_y = self.rect.y // self.tilesize
        # what's inside the tile
        self.content = cnt
        self.screen = screen
        self.__set_sprite()

    def __str__(self):
        return self.content

    def __set_sprite(self):
        """
        Sprites in .sprites folder must have same names as fields in Content class
        """
        try:
            for attr in dir(Content):
                v = getattr(Content, attr)
                if v == self.content:
                    self.sprite = pygame.image.load(f'sprites/{attr.lower()}.png')
                    break
        except:
            self.sprite = pygame.image.load('sprites/error_sprite.png')

    def draw(self):
        '''blits tile sprite on the exact coordinates of pygame window'''
        self.screen.blit(self.sprite, self.rect)
