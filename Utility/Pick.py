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

    def update_dimensions(self):
        self.width = WIN.get_width()
        self.height = WIN.get_height()

    def remove_previous_pointer(self):
        self.pointer = pygame.Rect((self.width - self.menu_width)//2, self.pointer_height, C.PADDING, C.PADDING//4)
        pygame.draw.rect(WIN, (0, 0, 0), self.pointer)
        pygame.display.flip()

    def draw_pointer(self):
        self.pointer = pygame.Rect((self.width - self.menu_width)//2, self.pointer_height, C.PADDING, C.PADDING//4)
        pygame.draw.rect(WIN, (255, 0, 0), self.pointer)
        pygame.display.flip()

    def update_pointer(self):
        self.remove_previous_pointer()
        self.draw_pointer()

    def draw_menu(self):
        self.menu_length = (len(self.things) + 2) * C.PADDING
        possible_widths = []
        for thing in self.things:
            try:
                text = FONT.render(str(thing.name), 1, C.WHITE)
            except:
                text = FONT.render(str(thing), 1, C.WHITE)
            possible_widths.append((text.get_width()*(2.2)))
        self.menu_width = (max(possible_widths)+(C.PADDING*3))
        self.menu = pygame.Rect((WIN.get_width() - self.menu_width)//2, 0, self.menu_width, self.menu_length)
        pygame.draw.rect(WIN, C.BLACK, self.menu)
        pygame.display.flip()

    def draw_list(self):
        self.update_dimensions()
        self.draw_menu()
        self.counter = 1
        for thing in self.things:
            text = FONT.render(str(self.counter)+" "+thing.name, 1, C.WHITE)
            WIN.blit(text, ((self.width - text.get_width())//2, C.PADDING * self.counter))
            self.counter += 1
        pygame.display.update()

    def draw_string_list(self):
        self.update_dimensions()
        self.draw_menu()
        self.counter = 1
        for thing in self.things:
            text = FONT.render(str(self.counter)+" "+str(thing), 1, C.WHITE)
            WIN.blit(text, ((self.width - text.get_width())//2, C.PADDING * self.counter))
            self.counter += 1
        pygame.display.update()

    def draw_skill_list(self):
        self.update_dimensions()
        self.draw_menu()
        self.counter = 1
        for thing in self.things:
            text = FONT.render(thing.name+" CD: "+str(thing.cooldown)+" Cost: "+str(thing.cost), 1, C.WHITE)
            WIN.blit(text, ((self.width - text.get_width())//2, C.PADDING * self.counter))
            self.counter += 1
        pygame.display.update()

    def draw_quest_list(self):
        self.update_dimensions()
        self.draw_wide_menu()
        self.counter = 1
        for thing in self.things:
            text = FONT.render(str(self.counter)+" "+str(thing), 1, C.WHITE)
            WIN.blit(text, ((self.width - text.get_width())//2, C.PADDING * self.counter))
            self.counter += 1
        pygame.display.update()

    def draw_wide_menu(self):
        self.menu_length = (len(self.things) + 2) * C.PADDING
        possible_widths = []
        for thing in self.things:
            try:
                text = FONT.render(str(thing.name), 1, C.WHITE)
            except:
                text = FONT.render(str(thing), 1, C.WHITE)
            possible_widths.append((text.get_width()*(4/3)))
        self.menu_width = (max(possible_widths)+(C.PADDING*2))
        self.menu = pygame.Rect((WIN.get_width() - self.menu_width)//2, 0, self.menu_width, self.menu_length)
        pygame.draw.rect(WIN, C.BLACK, self.menu)
        pygame.display.flip()

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
            self.pointer_height = C.PADDING * 1.375
            self.draw_pointer()
            chosen_index = 0
            while pick:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        pygame.event.clear()
                        if event.key == pygame.K_DOWN:
                            if chosen_index < len(self.things) - 1:
                                self.remove_previous_pointer()
                                self.pointer_height += C.PADDING
                                chosen_index += 1
                                self.draw_pointer()
                            else:
                                self.remove_previous_pointer()
                                self.pointer_height = C.PADDING * 1.375
                                chosen_index = 0
                                self.draw_pointer()
                        if event.key == pygame.K_UP:
                            if chosen_index > 0:
                                self.remove_previous_pointer()
                                self.pointer_height -= C.PADDING
                                chosen_index -= 1
                                self.draw_pointer()
                            else:
                                self.remove_previous_pointer()
                                self.pointer_height = (C.PADDING * (0.375 + len(self.things)))
                                chosen_index = len(self.things) - 1
                                self.draw_pointer()
                        if event.key == pygame.K_SPACE:
                            return self.things[chosen_index]

    def pick(self):
        if self.random_pick:
            return self.pick_randomly()
        else:
            try:
                self.draw_list()
            except:
                self.draw_string_list()
            return self.pick_from_list()

    def wide_pick(self):
        if self.random_pick:
            return self.pick_randomly()
        else:
            self.draw_quest_list()
            return self.pick_from_list()

    def pick_skill(self):
        if self.random_pick:
            return self.pick_randomly()
        else:
            self.draw_skill_list()
            return self.pick_from_list()