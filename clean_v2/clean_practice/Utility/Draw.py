import pygame
pygame.init()
from Config.Constants import Constants
C = Constants()
from Config.Image_Dict import *
I = Image_Dict()
clock = pygame.time.Clock()
FONT = pygame.font.SysFont("comicsans", C.REG_FONT)
WIN = pygame.display.set_mode((C.WIDTH, C.HEIGHT), pygame.RESIZABLE)

class Draw:
    def __init__(self):
        self.width = WIN.get_width()
        self.height = WIN.get_height()

    def draw_text(self, text: str):
        WIN.fill(C.BLACK)
        string = FONT.render(text, 1, C.WHITE)
        WIN.blit(string, ((self.width - string.get_width())//2, C.PADDING))
        pygame.display.update()
        pygame.time.delay(500)

    def update_heroes(self, heroes: list):
        self.heroes = heroes

    def update_spirits(self, spirits: list):
        self.spirits = spirits

    def update_monsters(self, monsters: list):
        self.monsters = monsters

    def draw_heroes(self):
        self.counter = 1
        for hero in self.heroes:
            sprite = I.IMAGES.get(hero.name)
            WIN.blit(sprite, (self.width - C.PADDING - sprite.get_width() * self.counter, self.height -  C.PADDING - sprite.get_height() * self.counter))
        pygame.display.update()

    def draw_monsters(self):
        self.counter = 1
        for monster in self.monsters:
            sprite = I.IMAGES.get(monster.name)
            WIN.blit(sprite, (sprite.get_width() * self.counter, self.height -  C.PADDING - sprite.get_height() * self.counter))
        pygame.display.update()

    def draw_spirits(self):
        self.counter = 1
        for spirit in self.spirits:
            sprite = I.IMAGES.get(spirit.name)
            WIN.blit(sprite, (self.width - C.PADDING - sprite.get_width() * self.counter, (self.height//2) - C.PADDING - sprite.get_height() * self.counter))
        pygame.display.update()

    def draw_battle_state(self):
        self.draw_heroes()
        self.draw_monsters()
        self.draw_spirits()

    def draw_monster_stats(self):
        self.counter = 1
        for monster in self.monsters:
            stat_text = FONT.render(monster.stats_text(), 1, C.WHITE)
            WIN.blit(stat_text, (C.PADDING, C.PADDING * self.counter))
        pygame.display.update()

    def draw_hero_stats(self):
        self.counter = 1
        for hero in self.heroes:
            stat_text = FONT.render(hero.stats_text(), 1, C.WHITE)
            WIN.blit(stat_text, (self.width - stat_text.get_width() - C.PADDING, C.PADDING * self.counter))
        pygame.display.update()

    def draw_battle_stats(self):
        self.draw_hero_stats()
        self.draw_monster_stats()