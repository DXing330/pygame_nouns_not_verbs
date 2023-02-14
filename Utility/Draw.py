import pygame
pygame.init()
from Config.Constants import Constants
C = Constants()
from Config.Image_Dict import *
I = Image_Dict()
clock = pygame.time.Clock()
FONT = pygame.font.SysFont("comicsans", C.REG_FONT)
SFONT = pygame.font.SysFont("comicsans", C.SMALL_FONT)
WIN = pygame.display.set_mode((C.WIDTH, C.HEIGHT), pygame.RESIZABLE)

class Draw:
    def __init__(self):
        self.width = WIN.get_width()
        self.height = WIN.get_height()

    def draw_bg_and_text(self, background, text: str, height = 1):
        self.draw_background(background)
        self.draw_text(text, height)

    def draw_text(self, text: str, height = 1):
        string = FONT.render(text, 1, C.WHITE)
        WIN.blit(string, ((self.width - string.get_width())//2, C.PADDING * height))
        pygame.display.update()

    def draw_background(self, background = None):
        self.width = WIN.get_width()
        self.height = WIN.get_height()
        if background == None:
            WIN.fill(C.BLACK)
        else:
            image = I.IMAGES.get(background)
            image = pygame.transform.scale(image, (self.width, self.height))
            WIN.blit(image, (0, 0))
        pygame.display.update()

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
            WIN.blit(sprite, (self.width - sprite.get_width() - C.PADDING * self.counter, self.height - C.PADDING - sprite.get_height() * self.counter))
            self.counter += 1
        pygame.display.update()

    def draw_monsters(self):
        self.counter = 1
        for monster in self.monsters:
            sprite = I.IMAGES.get(monster.name)
            text = FONT.render(monster.action, 1, C.WHITE)
            WIN.blit(sprite, (sprite.get_width() + C.PADDING * self.counter, self.height - (C.PADDING * self.counter) - (sprite.get_height() * self.counter)))
            WIN.blit(text, (sprite.get_width() - text.get_width()//4 + C.PADDING * self.counter, self.height - (C.PADDING * self.counter) - (sprite.get_height() * self.counter) - text.get_height()))
            self.counter += 1
        pygame.display.update()

    def draw_monsters_without_actions(self):
        self.counter = 1
        for monster in self.monsters:
            sprite = I.IMAGES.get(monster.name)
            WIN.blit(sprite, (sprite.get_width() + C.PADDING * self.counter, self.height - (C.PADDING * self.counter) - (sprite.get_height() * self.counter)))
            self.counter += 1
        pygame.display.update()

    def draw_spirits(self):
        self.counter = 1
        for spirit in self.spirits:
            sprite = I.IMAGES.get(spirit.name)
            WIN.blit(sprite, (self.width - C.PADDING - sprite.get_width() * self.counter, (self.height//2) - C.PADDING - sprite.get_height() * self.counter))
            self.counter += 1
        pygame.display.update()

    def draw_turn_order(self, battlers):
        self.counter = 1
        for battler in battlers:
            text = SFONT.render(str(self.counter)+" "+battler.name, 1, C.WHITE)
            WIN.blit(text, (C.PADDING, self.height//3 + (C.PADDING * self.counter)))
            self.counter += 1
        pygame.display.update()

    def draw_battle_state(self):
        self.draw_heroes()
        self.draw_monsters()
        self.draw_spirits()

    def draw_monster_stats(self):
        self.counter = 1
        for monster in self.monsters:
            stat_text = SFONT.render(monster.stats_text(), 1, C.WHITE)
            WIN.blit(stat_text, (C.PADDING, C.PADDING * self.counter))
            self.counter += 1
        pygame.display.update()

    def draw_hero_stats(self):
        self.counter = 1
        for hero in self.heroes:
            stat_text = SFONT.render(hero.stats_text(), 1, C.WHITE)
            WIN.blit(stat_text, (self.width - stat_text.get_width() - C.PADDING, C.PADDING * self.counter))
            self.counter += 1
        pygame.display.update()

    def draw_full_hero_stats(self, heroes):
        WIN.fill((0, 0, 0))
        self.counter = 1
        for hero in heroes:
            stat_text = FONT.render(hero.full_stats_text(), 1, C.WHITE)
            WIN.blit(stat_text, ((self.width - stat_text.get_width())//2, C.PADDING * self.counter))
            self.counter += 1
        pygame.display.update()
        view = True
        while view:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    view = False

    def draw_battle_stats(self):
        self.draw_hero_stats()
        self.draw_monster_stats()

    def draw_hero_options(self, hero):
        self.draw_text(hero.name+"'s Turn")
        self.draw_text("Attack", 2)
        self.draw_text("Items", 3)
        if len(hero.skill_list) > 0:
            self.draw_text("Skill", 4)

    def draw_item_options(self, bag):
        self.draw_text("Health Potions: "+str(bag.health_potions))
        self.draw_text("Energy Potions: "+str(bag.energy_potions), 2)

    def draw_quests(self, quests):
        self.counter = 1
        for quest in quests:
            if not quest.completed and not quest.failed:
                self.draw_text("Quest: "+quest.name+" L: "+quest.location+" R: "+quest.requirement+" S: "+quest.specifics+" A: "+str(quest.specifics_amount), self.counter)
                self.counter += 1

    def change_name(self, hero):
        edit = True
        user_text = ""
        while edit:
            self.draw_text(user_text)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        hero.real_name = str(user_text)
                        edit = False
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode

    def draw_corner_text(self, text):
        string = FONT.render(text, 1, C.WHITE)
        WIN.blit(string, (self.width - string.get_width() - C.PADDING, C.PADDING))
        pygame.display.update()