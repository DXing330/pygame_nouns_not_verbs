import random
import pygame

from Battle.Battle_Encounter import Monster_Encounter
pygame.init()

WIN = pygame.display.set_mode((1200, 800), pygame.RESIZABLE)

class Battle_Zone:
    def __init__(self, party, location):
        self.party = party
        self.location = location
        self.player = pygame.Rect(0, 0, 50, 50)
        self.counter = 0
        self.counter_limit = 0
        self.movement = 1
        self.height = WIN.get_height()
        self.width = WIN.get_width()

    def draw_overworld(self):
        self.height = WIN.get_height()
        self.width = WIN.get_width()
        WIN.fill((0, 0, 0))
        pygame.draw.rect(WIN, (100, 150, 150), pygame.Rect(self.width - self.width//6, self.height - self.width//6, self.width//6, self.width//6))
        pygame.draw.rect(WIN, (0, 255, 0), self.player)
        pygame.display.update()

    def reset_counter(self):
        self.counter = 0
        self.counter_limit = round(random.gauss((self.width+self.height)/self.location.dungeon_size, max(self.width, self.height)/self.location.dungeon_size))

    def battle_loop(self):
        danger = True
        self.draw_overworld()
        self.reset_counter()
        while danger:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.player.x > self.width - self.width//6 and self.player.y > self.width//6 - self.player.height:
                            danger = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and (self.player.x) > 0:
                self.player.x -= self.movement
                self.counter += self.movement
                self.draw_overworld()
            if keys[pygame.K_RIGHT] and (self.player.x) < (self.width - self.player.width):
                self.player.x += self.movement
                self.counter += self.movement
                self.draw_overworld()
            if keys[pygame.K_UP] and (self.player.y) > 0:
                self.player.y -= self.movement
                self.counter += self.movement
                self.draw_overworld()
            if keys[pygame.K_DOWN] and (self.player.y) < (self.height - self.player.height):
                self.player.y += self.movement
                self.counter += self.movement
                self.draw_overworld()
            if self.counter >= self.counter_limit:
                self.reset_counter()
                battle = Monster_Encounter(self.party, self.location, random.randint(1, self.location.dungeon_size), [], [])
                if self.location.boss and battle.amount == self.location.dungeon_size:
                    battle.boss = True
                battle.start_phase()
                self.draw_overworld()