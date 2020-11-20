import pygame
from constants import Content
from .moving_object import MovingObject

class Pacman(MovingObject):
    pacman_sprite = 'sprites/pacman.png'

    def __init__(self, game, x, y, speed):
        super().__init__(game, x, y, pygame.image.load(self.pacman_sprite), Content.PACMAN, speed)

    def process_move(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.shift_x = -1
            elif event.key == pygame.K_d:
                self.shift_x = 1
            if event.key == pygame.K_w:
                self.shift_y = -1
            elif event.key == pygame.K_s:
                self.shift_y = 1
            # print(self.shift_x, self.shift_y)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                self.shift_x = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                self.shift_y = 0
        self.move()

    def move(self):
        self.rect.x += self.speed * self.shift_x
        self.rect.y += self.speed * self.shift_y

    def check_collision(self):
        # ghost collision check
        # cherry collision check
        # dot collision check
        # power-up collision check
        # wall collision check
        pass

    def process_event(self, event):
        self.process_move(event)
