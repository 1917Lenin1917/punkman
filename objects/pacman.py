import pygame
from constants import Content
from .moving_object import MovingObject

class Pacman(MovingObject):
    pacman_sprite = 'sprites/pacman.png'

    def __init__(self, game, x, y, map_ref):
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
        # move log: print(self.real_x, self.real_y, self.map.tile_arr[self.real_y][self.real_x].content)
        self.update_pos()

    '''checks if next step Tile is not a Wall'''
    def is_able_to_move(self, x, y):
        '''дело в том, что в двумерной матрице первая координата - это строка или же Y, а вторая - X'''
        if self.map.tile_arr[self.real_y + y][self.real_x +x].content != Content.WALL:
            return True
        else:
            return False

    def process_logic(self):
        self.process_move()
