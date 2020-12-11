from .base import Ghost, MovementMode, Scatter
from objects import Map, Tile, Pacman
from typing import Tuple
from misc import clamp


class PinkyChase(MovementMode):
    def __init__(self, ghost, ttile_crds: Tuple[int, int]):
        super().__init__(ghost, ttile_crds)

    def update_ttile(self):
        x, y = self.ghost.pacman.real_x, self.ghost.pacman.real_y
        x += self.ghost.pacman.dir[0] * 2
        y += self.ghost.pacman.dir[1] * 2

        x = clamp(x, 0, 18)
        y = clamp(y, 0, 25)
        self.target_tile = self.ghost.map.tile_arr[y][x]


class Pinky(Ghost):
    ghost_sprite = 'pinky'

    def __init__(self, game, x, y, map_ref: Map, pacman_ref: Pacman, ttile_coords):
        super().__init__(game, x, y, map_ref, pacman_ref, ttile_coords, self.ghost_sprite)
        self.modes = [Scatter(self, ttile_coords), PinkyChase(self, ttile_coords)]

        self.can_leave = False
