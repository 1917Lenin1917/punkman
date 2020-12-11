from .base import Ghost, Scatter, MovementMode
from objects import Map, Pacman
from typing import Tuple
from misc import clamp
from constants import Content


class InkyChase(MovementMode):
    def __init__(self, ghost, ttile_crds: Tuple[int, int], blinky: Ghost):
        super().__init__(ghost, ttile_crds)
        self.blinky = blinky

    def update_ttile(self):
        x, y = self.ghost.pacman.real_x, self.ghost.pacman.real_y
        x += self.ghost.pacman.dir[0] * 2
        y += self.ghost.pacman.dir[1] * 2
        vec1 = (abs(x - self.blinky.real_x), abs(y - self.blinky.real_y))
        vec2 = (clamp(vec1[0], 0, 18), clamp(vec1[1], 0, 25))

        self.target_tile = self.ghost.map.tile_arr[vec2[1]][vec2[0]]


class Inky(Ghost):
    ghost_sprite = 'inky'

    def __init__(self, game, x, y, map_ref: Map, pacman_ref: Pacman, ttile_coords, blinky):
        super().__init__(game, x, y, map_ref, pacman_ref, ttile_coords, self.ghost_sprite)
        self.blinky = blinky
        self.modes = [Scatter(self, ttile_coords), InkyChase(self, ttile_coords, self.blinky)]

        self.can_leave = False
