import sys
sys.path.append("./Config/Constants")
from Constants import *
C = Constants()
import pygame
pygame.init()
import random
from dataclasses import dataclass
clock = pygame.time.Clock()
WIN = pygame.display.set_mode((C.WIDTH, C.HEIGHT), pygame.RESIZABLE)
FONT = pygame.font.SysFont("comicsans", 25)

@dataclass
class Pick:
    things : list
    pick_randomly : bool = True

    def draw_list(self):
        self.width = WIN.get_width()
        self.height = WIN.get_height()
        self.counter = 1
        for object in self.things:
            text = FONT.render(str(self.counter)+" "+object.name, 1, C.WHITE)
            WIN.blit(text, ((self.width - text.get_width())//2, C.PADDING * self.counter))
            self.counter += 1
        pygame.display.update()

    def pick_randomly(self):
        thing = self.things[random.randint(0, len(self.things) - 1)]
        return thing

    def pick_from_list(self):
        if len(self.things) <= 0:
            thing = None
            return thing
        elif len(self.things) == 1:
            thing = self.things[0]
            return thing
        if self.pick_randomly:
            return self.pick_randomly()
        self.pick = True
        while self.pick:
            pygame.event.clear()
            clock.tick(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        thing = self.list[0]
                        break
                    if event.key == pygame.K_2:
                        thing = self.list[1]                        
                        break
                    if event.key == pygame.K_3 and len(self.list) >= 3:
                        thing = self.list[2]                        
                        break
                    if event.key == pygame.K_4 and len(self.list) >= 4:
                        thing = self.list[3]                        
                        break
                    if event.key == pygame.K_5 and len(self.list) >= 5:
                        thing = self.list[4]                        
                        break
                    if event.key == pygame.K_6 and len(self.list) >= 6:
                        thing = self.list[5]                        
                        break
                    if event.key == pygame.K_7 and len(self.list) >= 7:
                        thing = self.list[6]                        
                        break
                    if event.key == pygame.K_8 and len(self.list) >= 8:
                        thing = self.list[7]                      
                        break
                    if event.key == pygame.K_9 and len(self.list) >= 9:
                        thing = self.list[8]             
                        break
        return thing

    def pick(self):
        self.draw_list()
        return self.pick_from_list()
