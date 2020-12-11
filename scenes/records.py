import pygame
from objects import ButtonObject
from scenes import BaseScene
from constants import Color
from objects import TextObject

class RecordsScene(BaseScene):
    records_file = 'records.txt'
    
    def create_objects(self) -> None:
        self.button_exit = ButtonObject(
            self.game,
            10, 25, 200, 50,
            Color.ORANGE, self.exit_to_menu, "Назад"
        )
        self.record_1 = TextObject(self.game, text='1) None', x=self.game.WIDTH // 2, y=self.game.HEIGHT // 2 - 50)
        self.record_2 = TextObject(self.game, text='2) None', x=self.game.WIDTH // 2, y=self.game.HEIGHT // 2)
        self.record_3 = TextObject(self.game, text='3) None', x=self.game.WIDTH // 2, y=self.game.HEIGHT // 2 + 50)
        self.objects = [self.button_exit, self.record_1, self.record_2, self.record_3]

    def on_activate(self):
        pass

    def exit_to_menu(self):
        self.game.set_scene(self.game.MENU_SCENE_INDEX)