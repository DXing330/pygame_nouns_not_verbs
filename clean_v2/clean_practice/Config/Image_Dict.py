import pygame
pygame.init()
import os
from Config.Constants import *
C = Constants()
# Characters
ANGEL = pygame.image.load(os.path.join("Assets", "angel.png"))
ANGEL = pygame.transform.scale(ANGEL, (C.PLAYER_SIZE//2, C.PLAYER_SIZE//2))
BEAST = pygame.image.load(os.path.join("Assets", "beast.png"))
BEAST = pygame.transform.scale(BEAST, (C.MONSTER_SIZE, C.MONSTER_SIZE))
IMP = pygame.image.load(os.path.join("Assets", "imp.png"))
IMP = pygame.transform.scale(IMP, (C.PLAYER_SIZE, C.PLAYER_SIZE))
GOBLIN = pygame.image.load(os.path.join("Assets", "goblin.png"))
GOBLIN = pygame.transform.scale(GOBLIN, (C.PLAYER_SIZE, C.PLAYER_SIZE))
GOLEM = pygame.image.load(os.path.join("Assets", "golem.png"))
GOLEM = pygame.transform.scale(GOLEM, (C.MONSTER_SIZE, C.MONSTER_SIZE))
BIG_GOLEM = pygame.transform.scale(GOLEM, (C.MONSTER_SIZE * 2, C.MONSTER_SIZE * 2))
SUMMONER = pygame.image.load(os.path.join("Assets", "summoner.png"))
SUMMONER = pygame.transform.scale(SUMMONER, (C.PLAYER_SIZE, C.PLAYER_SIZE))
TURRET = pygame.image.load(os.path.join("Assets", "turret.png"))
TURRET = pygame.transform.scale(TURRET, (C.PLAYER_SIZE, C.PLAYER_SIZE))
# Backgrounds
FOREST = pygame.image.load(os.path.join("Assets", "forest1.png"))


class Image_Dict:
    def __init__(self):
        self.IMAGES = {
        "Angel" : ANGEL, "Forest" : FOREST, "Goblin" : GOBLIN, "Golem" : GOLEM, "Imp" : IMP, "Summoner" : SUMMONER, "Turret" : TURRET
        }