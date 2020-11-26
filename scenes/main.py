from scenes import BaseScene
from objects import Map
from constants import Color
from objects import Pacman

class MainScene(BaseScene):
    def create_objects(self) -> None:
        self.objects = []
        self.objects.append(Map(self.game))
        self.objects.append(Pacman(self.game, 1, 1, self.objects[0])) # giving a map reference to pacman
        
