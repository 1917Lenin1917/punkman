import pygame
from objects import ButtonObject
from scenes import BaseScene
from constants import Color
from objects import TextObject

class RecordsScene(BaseScene):
    
    def create_objects(self) -> None:
        self.button_exit = ButtonObject(
            self.game,
            10, 25, 200, 50,
            Color.ORANGE, self.exit_to_menu, "Назад"
        )
        self.record_1 = TextObject(self.game, font_name='fonts/PressStart2P-Regular.ttf', text='1) None', x=self.game.WIDTH // 2, y=self.game.HEIGHT // 2 - 50)
        self.record_2 = TextObject(self.game, font_name='fonts/PressStart2P-Regular.ttf', text='2) None', x=self.game.WIDTH // 2, y=self.game.HEIGHT // 2)
        self.record_3 = TextObject(self.game, font_name='fonts/PressStart2P-Regular.ttf', text='3) None', x=self.game.WIDTH // 2, y=self.game.HEIGHT // 2 + 50)
        self.objects = [self.button_exit, self.record_1, self.record_2, self.record_3]

    def on_activate(self):
        records = []
        with open('records.txt') as r_file:
            # records = [i.strip() for i in r_file.readlines()]
            records = list(map(int, r_file.readlines()))
            records = sorted(records, reverse=True)
        if len(records)<3:
            for i in range(3 - len(records)):
                records.append(0)
        
        self.update_records_text(records)

    def exit_to_menu(self):
        self.game.set_scene(self.game.MENU_SCENE_INDEX)

    def update_records_text(self, records):
        self.record_1.update_text('1) ' + str(records[0]))
        self.record_2.update_text('2) ' + str(records[1]))
        self.record_3.update_text('3) ' + str(records[2]))