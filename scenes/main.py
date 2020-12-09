from scenes import BaseScene
from objects import Map, Pacman, Ghost, Blinky


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
