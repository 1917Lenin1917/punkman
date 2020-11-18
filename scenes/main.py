from scenes import BaseScene
from objects import Map
from constants import Color


class MainScene(BaseScene):
    def create_objects(self) -> None:
        self.objects = [Map(
          self.game
        )]
