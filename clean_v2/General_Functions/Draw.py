import pygame
pygame.init()
from dataclasses import dataclass
from Config.Constants.Constants import *
C = Constants()
from Config.Dictionaries.Image_Dict import *
I = Image_Dict()
WIN = pygame.display.set_mode((C.WIDTH, C.HEIGHT), pygame.RESIZABLE)
FONT = pygame.font.SysFont("comicsans", C.REG_TEXT)

@dataclass
class Draw_Screen:
    width = WIN.get_width()
    height = WIN.get_height()

    def draw_words(self, word : str):
        text = FONT.render(word, 1, C.WHITE)
        WIN.blit(text, ((self.width - text.get_width())//2, self.height//3))
        pygame.display.update()
        pygame.time.delay(500)

    def draw_heroes(self, heroes: list):
        self.counter = 1
        for hero in heroes:
            hero.sprite = I.IMAGES.get(hero.name)
            WIN.blit(hero.sprite, (self.width - (hero.sprite.get_width() * self.counter),
            self.height - (hero.sprite.get_height() * self.counter)))
            self.counter += 1
        pygame.display.update()


@dataclass
class Draw_Battle(Draw_Screen):

    def draw_monsters(self, monsters: list):
        self.counter = 1
        for monster in monsters:
            monster.sprite = I.IMAGES.get(monster.name)
            WIN.blit(monster.sprite, ((monster.sprite.get_width() * self.counter), self.height - (monster.sprite.get_height() * self.counter)))
            self.counter += 1
        pygame.display.update()