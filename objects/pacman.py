import pygame
from constants import Content
from .moving_object import MovingObject
from misc import clamp


class Pacman(MovingObject):
    pacman_sprite = 'sprites/pacman.png'

    def __init__(self, game, x, y, map_ref):
        self.lives = 3
        super().__init__(game, x, y, pygame.image.load(self.pacman_sprite), Content.PACMAN, map_ref)

    def process_move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and self.is_able_to_move(-1, 0): self.move(-1, 0)
        elif keys[pygame.K_d] and self.is_able_to_move(1, 0): self.move(1, 0)
        elif keys[pygame.K_w] and self.is_able_to_move(0, -1): self.move(0, -1)
        elif keys[pygame.K_s] and self.is_able_to_move(0, 1): self.move(0, 1)

    def move(self, x_increment, y_increment):
        self.real_x += x_increment
        self.real_y += y_increment
        # move log: 
        print(self.real_x, self.real_y, self.map.tile_arr[self.real_y][self.real_x].content)
        self.check_teleportation()
        self.update_pos()

    def check_teleportation(self):
        if self.map.teleport1 is None: return

        if self.real_x == self.map.teleport1[0] and self.real_y == self.map.teleport1[1]:
            self.real_x = self.map.teleport2[0]+1
            self.real_y = self.map.teleport2[1]
        elif self.real_x == self.map.teleport2[0] and self.real_y == self.map.teleport2[1]:
            self.real_x = self.map.teleport1[0]-1
            self.real_y = self.map.teleport1[1]

    def get_eaten(self):
        self.lives = clamp(self.lives-1, 0, 3)

    def process_logic(self):
        self.process_move()
