from .base import Ghost
from objects import Map, Tile, Pacman


class Blinky(Ghost):
    def __init__(self, game, x, y, map_ref: Map, pacman_ref: Pacman, ttile_coords, sprite_name=None):
        super().__init__(game, x, y, map_ref, pacman_ref, ttile_coords, sprite_name)
