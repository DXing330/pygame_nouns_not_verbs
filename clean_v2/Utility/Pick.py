import pygame
pygame.init()
import random
from dataclasses import dataclass
from Config.Constants import Constants
C = Constants()
clock = pygame.time.Clock()
FONT = pygame.font.SysFont("comicsans", C.REG_FONT)
WIN = pygame.display.set_mode((C.WIDTH, C.HEIGHT), pygame.RESIZABLE)


@dataclass
class Pick:
    things: list
    random_pick: bool = True

    def draw_list(self):
        self.counter = 1
        self.width = WIN.get_width()
        self.height = WIN.get_height()
        for thing in self.things:
            text = FONT.render(str(self.counter)+" "+thing.name, 1, C.WHITE)
            WIN.blit(text, ((self.width - text.get_width())//2, C.PADDING * self.counter))
            self.counter += 1
        pygame.display.update()

    def draw_string_list(self):
        self.counter = 1
        self.width = WIN.get_width()
        self.height = WIN.get_height()
        for thing in self.things:
            text = FONT.render(str(self.counter)+" "+str(thing), 1, C.WHITE)
            WIN.blit(text, ((self.width - text.get_width())//2, C.PADDING * self.counter))
            self.counter += 1
        pygame.display.update()

    def draw_skill_list(self):
        self.counter = 1
        self.width = WIN.get_width()
        self.height = WIN.get_height()
        for thing in self.things:
            text = FONT.render(str(self.counter)+" "+thing.name+" CD: "+str(thing.cooldown), 1, C.WHITE)
            WIN.blit(text, ((self.width - text.get_width())//2, C.PADDING * self.counter))
            self.counter += 1
        pygame.display.update()

    def pick_randomly(self):
        if len(self.things) == 0:
            return None
        return self.things[random.randint(0, len(self.things) - 1)]

    def pick_from_list(self):
        if len(self.things) == 0:
            return None
        elif len(self.things) == 1:
            return self.things[0]
        else:
            pick = True
            while pick:
                choice_list = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        pygame.event.clear()
                        try:
                            index = choice_list.index(event.key)
                            return self.things[index]
                        except:
                            pass

    def pick(self):
        if self.random_pick:
            return self.pick_randomly()
        else:
            try:
                self.draw_list()
            except:
                self.draw_string_list()
            return self.pick_from_list()

    def pick_skill(self):
        if self.random_pick:
            return self.pick_randomly()
        else:
            self.draw_skill_list()
            return self.pick_from_list()

    def pick_potion(self):
        pick = True
        while pick:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    pygame.event.clear()
                    if event.key == pygame.K_h:
                        choice = "Health"
                        return choice
                    if event.key == pygame.K_e:
                        choice = "Energy"
                        return choice