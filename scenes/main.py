from scenes import BaseScene
from objects import Map
from constants import Color
from objects import Pacman

class MainScene(BaseScene):
    def create_objects(self) -> None:
        self.objects = [Map(
          self.game
        ), Pacman(self.game, 1, 1, 3)]
