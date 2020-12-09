import pygame
from objects.moving_object import MovingObject
from constants import Content
from objects import Map, Tile, Pacman


class Ghost(MovingObject):
    ghost_sprite = 'sprites/blinky.png'

    def __init__(self, game, x, y, map_ref: Map, pacman_ref: Pacman, ttile_coords, sprite_name=None):
        if sprite_name is not None:
            self.ghost_sprite = f'sprites/{sprite_name}.png'
        super().__init__(game, x, y, pygame.image.load(self.ghost_sprite), Content.PINKY, map_ref)
        self.pacman = pacman_ref
        self.can_leave = True
        self.prev_dir = (-1, 0)
        self.dir = (-1, 0)
        self.target_tile = (map_ref.tile_arr[ttile_coords[1]][ttile_coords[0]])
        self.target_tile.sprite = pygame.image.load('sprites/error_sprite.png')

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

        if self.dir[0] != 0:
            possible_moves = (
                (self.map.tile_arr[self.real_y - 1][self.real_x], (-1, 0)),
                (self.map.tile_arr[self.real_y][self.real_x + self.dir[0]], (0, self.dir[0])),
                (self.map.tile_arr[self.real_y + 1][self.real_x], (1, 0)),
            )
        else:
            possible_moves = (
                (self.map.tile_arr[self.real_y + self.dir[1]][self.real_x], (self.dir[1], 0)),
                (self.map.tile_arr[self.real_y][self.real_x - 1], (0, -1)),
                (self.map.tile_arr[self.real_y][self.real_x + 1], (0, 1)),
            )
        possible_moves = tuple(map(
            lambda x: (x, self.dist_target(x[0])), possible_moves))
        possible_moves = tuple(filter(
            lambda x: x[0][0].content != Content.WALL, possible_moves))

        next_move = min(possible_moves, key=lambda x: x[1])
        self.prev_dir = self.dir
        self.dir = next_move[0][1][::-1]
        self.move(*self.dir)

    def dist_target(self, tile: Tile) -> float:
        """
        @param tile: tile on the map
        @return: distance from tile to target tile of the ghost
        """
        return ((tile.matrix_x - self.target_tile.matrix_x)**2 + (tile.matrix_y - self.target_tile.matrix_y)**2)**0.5

    def update_mode(self):
        """
            There are 4 waves of changes.
            1. Scatter for 7 seconds, then Chase for 20 seconds.
            2. Scatter for 7 seconds, then Chase for 20 seconds.
            3. Scatter for 5 seconds, then Chase for 20 seconds.
            4. Scatter for 5 seconds, then switch to Chase mode permanently.
        """
        pass

    def is_valid_dir(self, direction):
        return self.dir[0] != direction[0] * -1 if abs(self.dir[0]) == 1 else self.dir[1] != direction[1] * -1

    def process_logic(self):
        if self.can_leave: self.process_move()
