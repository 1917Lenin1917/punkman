from objects.tile import Tile
from constants import Content
from typing import List


class Map:
    map_path = 'pacman.map'

    def extract(self, map_path):
        tile_arr: List[List[Tile]] = []
        with open(map_path, 'r') as mp:
            tile_code_arr = [list(i.strip()) for i in mp.readlines()]
            for row in range(len(tile_code_arr)):
                tile_arr.append([Tile(col, row, tile_code_arr[row][col], self.game) for col in range(len(tile_code_arr[row]))])
        return tile_arr

    def __init__(self, game):
        self.game = game
        self.teleport1 = None
        self.teleport2 = None

        self.tile_arr = self.extract(self.map_path)
        self.eatable_count = sum([1 for arr in self.tile_arr for tile in arr if tile.content == Content.DOT or
                                                                                tile.content == Content.POWER_UP or
                                                                                tile.content == Content.CHERRY])
        self.check_teleport_pos()

    def process_draw(self):
        for i in range(len(self.tile_arr)):
            for j in range(len(self.tile_arr[i])):
                self.tile_arr[i][j].draw()

    def check_teleport_pos(self):
        for i in self.tile_arr:
            for j in i:
                if j.content == Content.TELEPORT:
                    if self.teleport1 is None:
                        self.teleport1 = j.matrix_x, j.matrix_y
                    elif self.teleport2 is None:
                        self.teleport2 = j.matrix_x, j.matrix_y
        print(self.teleport1, self.teleport2, sep='\n')

    def process_logic(self):
        pass

    def process_event(self, event):
        pass
