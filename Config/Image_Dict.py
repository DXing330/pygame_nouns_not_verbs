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
DEMON = pygame.image.load(os.path.join("Assets", "demon.png"))
DEMON = pygame.transform.scale(DEMON, (C.MONSTER_SIZE, C.MONSTER_SIZE))
GOBLIN = pygame.image.load(os.path.join("Assets", "goblin.png"))
GOBLIN = pygame.transform.scale(GOBLIN, (C.PLAYER_SIZE, C.PLAYER_SIZE))
BIG_GOBLIN = pygame.transform.scale(GOBLIN, (C.MONSTER_SIZE, C.MONSTER_SIZE))
GOLEM = pygame.image.load(os.path.join("Assets", "golem.png"))
GOLEM = pygame.transform.scale(GOLEM, (C.MONSTER_SIZE, C.MONSTER_SIZE))
IMP = pygame.image.load(os.path.join("Assets", "imp.png"))
IMP = pygame.transform.scale(IMP, (C.PLAYER_SIZE, C.PLAYER_SIZE))
ORC = pygame.image.load(os.path.join("Assets", "orc.png"))
ORC = pygame.transform.scale(ORC, (C.MONSTER_SIZE, C.MONSTER_SIZE))
SERPENT = pygame.image.load(os.path.join("Assets", "vena.png"))
SERPENT = pygame.transform.scale(SERPENT, (C.PLAYER_SIZE, C.PLAYER_SIZE))
SUMMONER = pygame.image.load(os.path.join("Assets", "summoner.png"))
SUMMONER = pygame.transform.scale(SUMMONER, (C.PLAYER_SIZE, C.PLAYER_SIZE))
TROLL = pygame.image.load(os.path.join("Assets", "troll.png"))
TROLL = pygame.transform.scale(TROLL, (C.MONSTER_SIZE, C.MONSTER_SIZE))
TURRET = pygame.image.load(os.path.join("Assets", "turret.png"))
TURRET = pygame.transform.scale(TURRET, (C.PLAYER_SIZE, C.PLAYER_SIZE))
VAMPIRE = pygame.image.load(os.path.join("Assets", "vampire.png"))
VAMPIRE = pygame.transform.scale(VAMPIRE, (C.PLAYER_SIZE, C.PLAYER_SIZE))
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
        "Angel" : ANGEL, "Cave" : CAVE, "Demon" : DEMON, "Forest" : FOREST, "Goblin" : GOBLIN, "Golem" : GOLEM, "Guild" : GUILD, "Hob Goblin" : BIG_GOBLIN, "Hunter" : WARRIOR, "Imp" : IMP, "Orc" : ORC, "Map" : MAP, "Serpent" : SERPENT, "Smith" : SMITH, "Summoner" : SUMMONER, "Troll" : TROLL, "Turret" : TURRET, "Vampire" : VAMPIRE, "Village" : VILLAGE, "Warrior" : WARRIOR, "Werewolf" : BEAST, "Wolf" : SMALL_BEAST
        }