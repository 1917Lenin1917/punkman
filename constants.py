import pygame
from enum import Enum

# https://www.pygame.org/docs/ref/color.html
# https://github.com/pygame/pygame/blob/master/src_py/colordict.py

class Color:
    RED = pygame.color.Color('red')
    BLUE = pygame.color.Color('blue')
    GREEN = pygame.color.Color('green')
    BLACK = pygame.color.Color('black')
    WHITE = pygame.color.Color('white')
    ORANGE = pygame.color.Color('orange')
    YELLOW = pygame.color.Color('yellow')

class Content(Enum):
    EMPTY = ' '
    WALL = '#'
    CHERRY = '.'
    POWER_UP = '0'
    BLINKY = 'b'
    PINKY = 'p'
    INKY = 'i'
    CLYDE = 'c'
    PACMAN = 'm'