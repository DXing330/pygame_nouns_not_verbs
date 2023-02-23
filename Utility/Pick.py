import pygame
pygame.init()
import random
from Config.Constants import Constants
C = Constants()
clock = pygame.time.Clock()
FONT = pygame.font.SysFont("comicsans", C.REG_FONT)
WIN = pygame.display.set_mode((C.WIDTH, C.HEIGHT), pygame.RESIZABLE)


class Pick:
    def __init__(self, things: list, random_pick: bool = True):
        self.things = things
        self.random_pick = random_pick
        self.update_dimensions()

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

    def draw_list(self, things, key = 0):
        self.update_dimensions()
        possible_widths = []
        texts = []
        self.counter = 1
        for thing in things:
            if key == 0:
                try:
                    text = FONT.render(str(thing.name), 1, C.WHITE)
                except:
                    text = FONT.render(str(thing), 1, C.WHITE)
            elif key == 1:
                text = FONT.render(thing.name+" CD: "+str(thing.cooldown)+" Cost: "+str(thing.cost), 1, C.WHITE)
            elif key == 2:
                text = FONT.render(str(thing), 1, C.WHITE)
            if key != 2:
                possible_widths.append((text.get_width()*(3/2)))
            elif key == 2:
                possible_widths.append((text.get_width()*(4/3)))
            texts.append(text)
        self.menu_width = max(self.menu_width, (max(possible_widths)+(C.PADDING*3)))
        self.menu = pygame.Rect((WIN.get_width() - self.menu_width)//2, 0, self.menu_width, self.menu_length)
        pygame.draw.rect(WIN, C.BLACK, self.menu)
        self.counter = 1
        for dtext in texts:
            WIN.blit(dtext, ((self.width - dtext.get_width())//2, C.PADDING * self.counter))
            self.counter += 1
        pygame.display.update()

    def split_list(self, length):
        new_list = []
        if len(self.things) > length:
            for number in range(length):
                new_list.append(self.things[number])
            del self.things[0:length]
        elif len(self.things) <= length:
            new_list = self.things
            self.things = []
        return new_list

    def make_longer_list(self):
        # Can't have the length go off the screen.
        self.max_length = (self.height//C.PADDING) - 2
        if len(self.things) > self.max_length:
            self.menu_length = (self.max_length + 1) * C.PADDING
        else:
            self.menu_length = (len(self.things)+2) * C.PADDING
        self.menu_width = 0
        # Split up the list into different pieces.
        self.list_of_lists = []
        while len(self.things) > 0:
            new_list = self.split_list(self.max_length)
            self.list_of_lists.append(new_list)

    def pick_from_list(self, key = 0):
        pick = True
        self.draw_list(self.list_of_lists[0], key)
        self.pointer_height = C.PADDING * 1.375
        self.draw_pointer()
        chosen_index = 0
        page = 0
        while pick:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    pygame.event.clear()
                    if event.key == pygame.K_SPACE:
                        return self.list_of_lists[page][chosen_index]
                    if event.key == pygame.K_DOWN:
                        self.remove_previous_pointer()
                        if chosen_index < len(self.list_of_lists[page]) - 1:
                            self.pointer_height += C.PADDING
                            chosen_index += 1
                        else:
                            self.pointer_height = C.PADDING * 1.375
                            chosen_index = 0
                        self.draw_pointer()
                    if event.key == pygame.K_UP:
                        self.remove_previous_pointer()
                        if chosen_index > 0:
                            self.pointer_height -= C.PADDING
                            chosen_index -= 1
                        else:
                            self.pointer_height = (C.PADDING * (0.375 + len(self.list_of_lists[page])))
                            chosen_index = len(self.list_of_lists[page]) - 1
                        self.draw_pointer()
                    if event.key == pygame.K_LEFT and page > 0:
                        page -= 1
                        chosen_index = 0
                        self.pointer_height = C.PADDING * 1.375
                        self.draw_list(self.list_of_lists[page], key)
                        self.draw_pointer()
                    if event.key == pygame.K_RIGHT and page < len(self.list_of_lists) - 1:
                        page += 1
                        chosen_index = 0
                        self.pointer_height = C.PADDING * 1.375
                        self.draw_list(self.list_of_lists[page], key)
                        self.draw_pointer()

    def pick_randomly(self):
        if len(self.things) == 0:
            return None
        return self.things[random.randint(0, len(self.things) - 1)]

    def pick(self, key = 0):
        if self.random_pick:
            return self.pick_randomly()
        elif len(self.things) == 0:
            return None
        elif len(self.things) == 1:
            return self.things[0]
        else:
            self.make_longer_list()
            return self.pick_from_list(key)