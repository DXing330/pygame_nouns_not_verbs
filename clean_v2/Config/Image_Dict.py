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
SMALL_BEAST = pygame.transform.scale(BEAST, (C.PLAYER_SIZE, C.PLAYER_SIZE))
IMP = pygame.image.load(os.path.join("Assets", "imp.png"))
IMP = pygame.transform.scale(IMP, (C.PLAYER_SIZE, C.PLAYER_SIZE))
GOBLIN = pygame.image.load(os.path.join("Assets", "goblin.png"))
GOBLIN = pygame.transform.scale(GOBLIN, (C.PLAYER_SIZE, C.PLAYER_SIZE))
BIG_GOBLIN = pygame.transform.scale(GOBLIN, (C.MONSTER_SIZE, C.MONSTER_SIZE))
GOLEM = pygame.image.load(os.path.join("Assets", "golem.png"))
GOLEM = pygame.transform.scale(GOLEM, (C.MONSTER_SIZE, C.MONSTER_SIZE))
BIG_GOLEM = pygame.transform.scale(GOLEM, (C.MONSTER_SIZE * 2, C.MONSTER_SIZE * 2))
SUMMONER = pygame.image.load(os.path.join("Assets", "summoner.png"))
SUMMONER = pygame.transform.scale(SUMMONER, (C.PLAYER_SIZE, C.PLAYER_SIZE))
TROLL = pygame.image.load(os.path.join("Assets", "troll.png"))
TROLL = pygame.transform.scale(TROLL, (C.PLAYER_SIZE * 2, C.PLAYER_SIZE * 2))
TURRET = pygame.image.load(os.path.join("Assets", "turret.png"))
TURRET = pygame.transform.scale(TURRET, (C.PLAYER_SIZE, C.PLAYER_SIZE))
WARRIOR = pygame.image.load(os.path.join("Assets", "warrior.png"))
WARRIOR = pygame.transform.scale(WARRIOR, (C.PLAYER_SIZE, C.PLAYER_SIZE))
# Backgrounds
FOREST = pygame.image.load(os.path.join("Assets", "forest1.png"))
CAVE = pygame.image.load(os.path.join("Assets", "cave.png"))
GUILD = pygame.image.load(os.path.join("Assets", "guild.png"))
MAP = pygame.image.load(os.path.join("Assets", "map.png"))
SMITH = pygame.image.load(os.path.join("Assets", "smith.png"))
VILLAGE = pygame.image.load(os.path.join("Assets", "village.png"))


class Image_Dict:
    def __init__(self):
        self.IMAGES = {
        "Angel" : ANGEL, "Cave" : CAVE, "Forest" : FOREST, "Goblin" : GOBLIN, "Golem" : GOLEM, "Guild" : GUILD, "Hob Goblin" : BIG_GOBLIN, "Imp" : IMP, "Map" : MAP, "Smith" : SMITH, "Summoner" : SUMMONER, "Troll" : TROLL, "Turret" : TURRET, "Village" : VILLAGE, "Warrior" : WARRIOR, "Werewolf" : BEAST, "Wolf" : SMALL_BEAST
        }