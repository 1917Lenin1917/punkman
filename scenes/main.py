from scenes import BaseScene
from objects import Map, Pacman, Ghost, Blinky, TextObject


class MainScene(BaseScene):
    def create_objects(self) -> None:
        self.objects = [Map(self.game)]
        self.objects.extend([
            Pacman(self.game, 1, 4, self.objects[0])])
        self.objects.extend([
            Blinky(self.game, 14, 14, self.objects[0], self.objects[1], (25, 1), 'blinky'),
            Ghost(self.game, 14, 14, self.objects[0], self.objects[1], (2, 1), 'pinky'),
            Ghost(self.game, 14, 14, self.objects[0], self.objects[1], (0, 35), 'inky'),
            Ghost(self.game, 14, 14, self.objects[0], self.objects[1], (26, 35), 'clyde'),
        ])
        self.objects.extend([
            TextObject(self.game, 'fonts/PressStart2P-Regular.ttf', is_sys=False, text='Score:0', x=100, y=20)
        ])

    def pacman_ghost_collision(self):
        collisions = list(map(lambda x: x.pacman_collision(), self.objects[2:6]))
        if True in collisions:
            self.objects[1].get_eaten()
            print(f'Lives left: {self.objects[1].lives}')
            if self.objects[1].lives == 0:
                print('GAME OVER')
                self.game.exit_game()
            self.objects[1].respawn()
            for ghost in self.objects[2:6]:
                ghost.respawn()

    def additional_logic(self):
        self.pacman_ghost_collision()

        if self.objects[1].dots_eaten != self.objects[0].dot_count:
            print(f'Game score is {self.objects[1].points}')
            return

        print(f'GAME END. THE FINAL SCORE IS {self.objects[1].points}')
