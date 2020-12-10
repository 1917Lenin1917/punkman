import pygame
from constants import Content
from .moving_object import MovingObject
from misc import clamp
from objects import Map


class Pacman(MovingObject):
    pacman_sprite = 'sprites/pacman.png'

    def __init__(self, game, x, y, map_ref: Map):
        super().__init__(game, x, y, pygame.image.load(self.pacman_sprite), Content.PACMAN, map_ref)
        self.points = 0
        self.dots_eaten = 0
        self.lives = 3

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
        # print(self.real_x, self.real_y, self.map.tile_arr[self.real_y][self.real_x].content)
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

    def eat(self):
        if self.map.tile_arr[self.real_y][self.real_x].content == Content.DOT:
            self.points += 10
            self.dots_eaten += 1
            self.map.tile_arr[self.real_y][self.real_x].content = Content.EMPTY
            self.map.tile_arr[self.real_y][self.real_x].set_sprite()

    def process_logic(self):
        self.eat()
        self.process_move()
