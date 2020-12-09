from .base import Ghost
from objects import Map, Tile, Pacman

class Blinky(Ghost):
    def __init__(self, game, x, y, map_ref: Map, pacman_ref: Pacman, ttile_coords, sprite_name=None):
        super().__init__(game, x, y, map_ref, pacman_ref, ttile_coords, sprite_name)

    def process_logic(self):
        self.target_tile = (self.map.tile_arr[self.pacman.real_y][self.pacman.real_x])
        if self.can_leave: self.process_move()
