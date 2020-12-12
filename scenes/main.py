from scenes import BaseScene
from objects import Map, Pacman, TextObject
from objects import Ghost, Blinky, Pinky, Inky, Clyde


class MainScene(BaseScene):
    def create_objects(self) -> None:
        self.map = Map(self.game)
        self.pacman = Pacman(self.game, 9, 18, self.map)

        self.blinky = Blinky(self.game, 9, 10, self.map, self.pacman, (1, 1))
        self.pinky  = Pinky(self.game, 9, 12, self.map, self.pacman, (18, 1))
        self.inky = Inky(self.game, 9, 12, self.map, self.pacman, (1, 24), self.blinky)
        self.clyde = Clyde(self.game, 9, 10, self.map, self.pacman, (18, 24))

        self.ghosts = [self.blinky, self.pinky, self.inky, self.clyde]

        self.objects.extend([
            self.map,
            self.pacman
        ])
        self.objects.extend(self.ghosts)
        self.objects.extend([
            TextObject(self.game, 'fonts/PressStart2P-Regular.ttf', is_sys=False, text='Score:0', x=110, y=20),
            TextObject(self.game, 'fonts/PressStart2P-Regular.ttf', is_sys=False, text='Lives:0', font_size=30, x=110, y=870)
        ])

    def pacman_ghost_collision(self):
        collisions = list(map(lambda x: x.pacman_collision(), self.ghosts))
        if True in collisions:
            self.pacman.get_eaten()
            if self.pacman.lives == 0:
                self.save_record()
                self.game.set_scene(self.game.RECORDS_SCENE_INDEX)
            self.pacman.respawn()
            for ghost in self.ghosts:
                ghost.respawn()

    def update_stats(self):
        p = self.pacman.points
        l = self.pacman.lives
        self.objects[6].update_text(f'{" "*len(str(p))}Score:{p}')
        self.objects[7].update_text(f'Lives:{l}')

    def is_win(self):
        if self.map.eatable_count == self.pacman.eaten:
            self.save_record()
            self.game.set_scene(self.game.RECORDS_SCENE_INDEX)

    def additional_logic(self):
        self.pacman_ghost_collision()
        self.update_stats()
        self.is_win()

    def save_record(self):
        with open('records.txt', 'a') as r_file:
            r_file.write(str(self.objects[1].points) + '\n')

    def on_activate(self):
        self.pacman.lives = 10
        self.pacman.eaten = 0
        self.pacman.points = 0
        self.map.tile_arr = self.map.extract(self.map.map_path)  # should be a method in Map
