from .base import Ghost, MovementMode, Scatter
from objects import Map, Tile, Pacman
from typing import Tuple


class BlinkyChase(MovementMode):
    def __init__(self, ghost, ttile_crds: Tuple[int, int]):
        super().__init__(ghost, ttile_crds)

    def update_ttile(self):
        x, y = self.ghost.pacman.real_x, self.ghost.pacman.real_y
        self.target_tile = self.ghost.map.tile_arr[y][x]


class Blinky(Ghost):
    ghost_sprite = 'blinky'

    def __init__(self, game, x, y, map_ref: Map, pacman_ref: Pacman, ttile_coords):
        super().__init__(game, x, y, map_ref, pacman_ref, ttile_coords, self.ghost_sprite)
        self.modes = [Scatter(self, ttile_coords), BlinkyChase(self, ttile_coords)]

