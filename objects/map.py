from objects.tile import Tile

class Map:
    map_path = 'pacman.map'
    @staticmethod
    def extract(map_path):
        tile_arr = []
        with open(map_path, 'r') as mp:
            tile_code_arr = [list(i.strip()) for i in mp.readlines()]
            for row in range(len(tile_code_arr)):
                tile_arr.append([Tile(col, row, tile_code_arr[row][col]) for col in range(len(tile_code_arr[row]))])

        return tile_arr

    def __init__(self):
        self.tile_arr = self.extract(self.map_path)

    def draw(self):
        '''draws each tile of map from tile array'''
        for i in range(len(self.tile_arr)):
            self.tile_arr[i].draw()
