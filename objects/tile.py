import pygame
from constants import Content, tilesize

class Tile:

    def __init__(self, x, y, cnt, game):
        # Rect object for hitboxing
        self.rect = pygame.rect.Rect(x*tilesize, y*tilesize, tilesize, tilesize)
        # real matrix coordinates
        self.matrix_x = self.rect.x
        self.matrix_y = self.rect.y
        # what's inside the tile
        self.content = cnt
        self.game = game
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
        self.game.screen.blit(self.sprite, self.rect)
