import pygame
from objects.moving_object import MovingObject
from constants import Content
from objects import Map, Tile, Pacman
from typing import Tuple
import time


class MovementMode:
    """
        A data struct for easy ghost behaviour changes
    """
    def __init__(self, ghost, ttile_crds: Tuple[int, int]):
        self.ghost: Ghost = ghost
        self.map = self.ghost.map
        self.target_tile = self.ghost.map.tile_arr[ttile_crds[1]][ttile_crds[0]]

    def next_move(self, is_first=False) -> Tuple[int, int]:
        self.update_ttile()

        if is_first:
            x, y = self.ghost.dir
            return x * -1, y * -1

        if self.ghost.dir[0] != 0:
            possible_moves = (
                (self.map.tile_arr[self.ghost.real_y - 1][self.ghost.real_x], (-1, 0)),
                (self.map.tile_arr[self.ghost.real_y][self.ghost.real_x + self.ghost.dir[0]], (0, self.ghost.dir[0])),
                (self.map.tile_arr[self.ghost.real_y + 1][self.ghost.real_x], (1, 0)),
            )
        else:
            possible_moves = (
                (self.map.tile_arr[self.ghost.real_y + self.ghost.dir[1]][self.ghost.real_x], (self.ghost.dir[1], 0)),
                (self.map.tile_arr[self.ghost.real_y][self.ghost.real_x - 1], (0, -1)),
                (self.map.tile_arr[self.ghost.real_y][self.ghost.real_x + 1], (0, 1)),
            )
        possible_moves = tuple(map(
            lambda x: (x, self.dist_target(x[0])), possible_moves))
        possible_moves = tuple(filter(
            lambda x: x[0][0].content != Content.WALL and x[0][0].content != Content.TELEPORT, possible_moves))

        if len(possible_moves) != 0:
            next_move = min(possible_moves, key=lambda x: x[1])
            return next_move[0][1][::-1]
        return self.ghost.dir[0] * -1, self.ghost.dir[1] * -1

    def update_ttile(self):
        pass

    def additional_logic(self):
        pass

    def dist_target(self, tile: Tile) -> float:
        """
        @param tile: tile on the map
        @return: distance from tile to target tile of the ghost
        """
        return ((tile.matrix_x - self.target_tile.matrix_x)**2 + (tile.matrix_y - self.target_tile.matrix_y)**2)**0.5


class Scatter(MovementMode):
    """
        Scatter mode is the same for all of the ghosts
    """
    def __init__(self, ghost, ttile_crds: Tuple[int, int]):
        super().__init__(ghost, ttile_crds)

    def update_ttile(self):
        self.target_tile = self.target_tile


class Frightened(MovementMode):
    def __init__(self, ghost, ttile_crds: Tuple[int, int]):
        super().__init__(ghost, ttile_crds)


class Ghost(MovingObject):
    def __init__(self, game, x, y, map_ref: Map, pacman_ref: Pacman, ttile_coords, sprite_name):
        self.ghost_sprite = f'sprites/ghosts/alive/{sprite_name}.png'
        super().__init__(game, x, y, pygame.image.load(self.ghost_sprite), Content.PINKY, map_ref)
        self.pacman = pacman_ref
        self.can_leave = True
        self.prev_dir = (-1, 0)
        self.dir = (0, 0)
        self.modes = [Scatter(self, ttile_coords), Scatter(self, ttile_coords), Frightened(self, ttile_coords)]
        self.ctime = -1
        self.mode_time = [7, 10, 7, 10, 5, 10, 5]
        self.selected_mode = 0
        self.last_time = 0  # needed to reset the time after death of the punkman
        # self.target_tile.sprite = pygame.image.load('sprites/error_sprite.png')

    def move(self, x_increment, y_increment):
        self.real_x += x_increment
        self.real_y += y_increment
        self.update_pos()

    def process_move(self):
        # movement rules:
        # 1. change dir priority
        # 2. never change dir 180
        # 3. when changing directions choose cell which is closer to the target cell
        # pretty much it
        self.prev_dir = self.dir
        self.dir = self.modes[self.selected_mode].next_move()

        if self.is_able_to_move(*self.dir):
            self.move(*self.dir)

    def update_mode(self):
        """
            There are 4 waves of changes.
            1. Scatter for 7 seconds, then Chase for 20 seconds.
            2. Scatter for 7 seconds, then Chase for 20 seconds.
            3. Scatter for 5 seconds, then Chase for 20 seconds.
            4. Scatter for 5 seconds, then switch to Chase mode permanently.
        """
        if self.ctime == -1:
            self.ctime = time.time()
            return
        delta = time.time() - self.ctime

        if delta > self.mode_time[0]:
            self.selected_mode = abs(self.selected_mode - 1)  # Switches between 0 and 1
            self.last_time = self.mode_time.pop(0)
            self.ctime = time.time()

            print('Switched modes')

    def pacman_collision(self):
        return self.real_x == self.pacman.real_x and self.real_y == self.pacman.real_y

    def is_valid_dir(self, direction):
        return self.dir[0] != direction[0] * -1 if abs(self.dir[0]) == 1 else self.dir[1] != direction[1] * -1

    def respawn_logic(self):
        self.selected_mode = 0
        self.ctime = time.time()
        if self.last_time != 0:
            self.mode_time.insert(0, self.last_time)

    def process_logic(self):
        if not self.can_leave: return

        self.update_mode()
        self.process_move()

