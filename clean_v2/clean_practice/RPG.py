import pygame
pygame.init()
import sys
sys.path.append("./Battle")
sys.path.append("./Characters")
sys.path.append("./Config")
sys.path.append("./Skills")
sys.path.append("./Utility")
from Battle.Battle_Encounter import *
from Characters.Party import *
WIN = pygame.display.set_mode((C.WIDTH, C.HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()


class RPG_GAME:
    def __init__(self):
        self.party : Party = Party()
        self.locations = []
    
    def start_game(self):
        start = True
        while start:
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    start = False
                    pygame.quit()
                if event == pygame.KEYDOWN:
                    pygame.event.clear()
                    if event.key == pygame.K_n:
                        self.party.new_party()
                        start = False
                    if event.key == pygame.K_c:
                        self.party.load()
                        start = False
        self.game_loop()
        
    def game_loop(self):
        game = True
        while game:
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    game = False
                    pygame.quit()