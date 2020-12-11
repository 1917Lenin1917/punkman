from .base import Ghost, MovementMode, Scatter
from objects import Map, Pacman
from typing import Tuple


class ClydeChase(MovementMode):
    def __init__(self, ghost, ttile_crds: Tuple[int, int]):
        super().__init__(ghost, ttile_crds)
        self.def_tile = self.target_tile

    def update_ttile(self):
        x, y = self.ghost.pacman.real_x, self.ghost.pacman.real_y
        ghost_tile = self.map.tile_arr[self.ghost.real_y][self.ghost.real_x]
        pacman_dist = self.dist(self.map.tile_arr[y][x], ghost_tile)
        print(f'Clyde-Pacman dist: {pacman_dist}')
        if pacman_dist > 6:
            self.target_tile = self.ghost.map.tile_arr[y][x]
            return

        self.target_tile = self.def_tile

    def dist(self, t1, t2):
        return ((t1.matrix_x - t2.matrix_x) ** 2 + (
                t1.matrix_y - t2.matrix_y) ** 2) ** 0.5

class Clyde(Ghost):
    ghost_sprite = 'clyde'

    def __init__(self, game, x, y, map_ref: Map, pacman_ref: Pacman, ttile_coords):
        super().__init__(game, x, y, map_ref, pacman_ref, ttile_coords, self.ghost_sprite)
        self.modes = [Scatter(self, ttile_coords), ClydeChase(self, ttile_coords)]
