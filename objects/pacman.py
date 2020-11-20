import pygame
from constants import Content
from .moving_object import MovingObject

class Pacman(MovingObject):
    pacman_sprite = 'sprites/pacman.png'

    def __init__(self, game, x, y):
        super().__init__(game, x, y, pygame.image.load(self.pacman_sprite), Content.PACMAN)

    def process_move(self, x, y):
        # if self.real_x + x, self.real_y + y != wall: then self.move(x, y)
        pass

    def check_collision(self):
        # ghost collision check
        # cherry collision check
        # dot collision check
        # power-up collision check
        # wall collision check
        pass 

