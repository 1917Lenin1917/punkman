from scenes import BaseScene
from objects import Map, Pacman, Ghost, Blinky, TextObject


class MainScene(BaseScene):
    def create_objects(self) -> None:
        self.objects = [Map(self.game)]
        self.objects.extend([
            Pacman(self.game, 9, 18, self.objects[0])])
        self.objects.extend([
            Blinky(self.game, 9, 9,  self.objects[0], self.objects[1], (1, 1), 'blinky'),
            Ghost(self.game, 9, 9, self.objects[0], self.objects[1], (18, 1), 'pinky'),
            Ghost(self.game, 9, 9, self.objects[0], self.objects[1], (1, 24), 'inky'),
            Ghost(self.game, 9, 9, self.objects[0], self.objects[1], (18, 24), 'clyde'),
        ])
        self.objects.extend([
            TextObject(self.game, 'fonts/PressStart2P-Regular.ttf', is_sys=False, text='Score:0', x=110, y=20),
            TextObject(self.game, 'fonts/PressStart2P-Regular.ttf', is_sys=False, text='Lives:0', font_size=30, x=110, y=870)
        ])

    def pacman_ghost_collision(self):
        collisions = list(map(lambda x: x.pacman_collision(), self.objects[2:6]))
        if True in collisions:
            self.objects[1].get_eaten()
            if self.objects[1].lives == 0:
                self.save_record()
                self.game.set_scene(self.game.RECORDS_SCENE_INDEX)
            self.objects[1].respawn()
            for ghost in self.objects[2:6]:
                ghost.respawn()

    def update_stats(self):
        p = self.objects[1].points
        l = self.objects[1].lives
        self.objects[6].update_text(f'{" "*len(str(p))}Score:{p}')
        self.objects[7].update_text(f'Lives:{l}')

    def additional_logic(self):
        self.pacman_ghost_collision()
        self.update_stats()

    def save_record(self):
        with open('records.txt', 'a') as r_file:
            r_file.write(str(self.objects[1].points) + '\n')

    def on_activate(self):
        self.objects[1].lives = 3
