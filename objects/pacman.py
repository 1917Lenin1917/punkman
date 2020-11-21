import pygame
from constants import Content
from .moving_object import MovingObject

class Pacman(MovingObject):
    pacman_sprite = 'sprites/pacman.png'

    def __init__(self, game, x, y, speed):
        super().__init__(game, x, y, pygame.image.load(self.pacman_sprite), Content.PACMAN)

    def process_move(self, event):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]: self.move(-1, 0)
        elif keys[pygame.K_d]: self.move(1, 0)
        elif keys[pygame.K_w]: self.move(0, -1)
        elif keys[pygame.K_s]: self.move(0, 1)

    def move(self, x, y):
        self.real_x += x
        self.real_y += y
        print(self.real_x, self.real_y)
        self.update_pos()

    def process_event(self, event):
        self.process_move(event)
