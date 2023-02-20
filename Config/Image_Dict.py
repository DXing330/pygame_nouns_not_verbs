import pygame
pygame.init()
import os
from Config.Constants import *
C = Constants()
# Characters
ANGEL = pygame.image.load(os.path.join("Assets", "angel.png"))
ANGEL = pygame.transform.scale(ANGEL, (C.PLAYER_SIZE, C.PLAYER_SIZE))
BEAST = pygame.image.load(os.path.join("Assets", "beast.png"))
BEAST = pygame.transform.scale(BEAST, (C.MONSTER_SIZE, C.MONSTER_SIZE))
SMALL_BEAST = pygame.transform.scale(BEAST, (C.PLAYER_SIZE, C.PLAYER_SIZE))
DEMON = pygame.image.load(os.path.join("Assets", "demon.png"))
DEMON = pygame.transform.scale(DEMON, (C.BIG_MONSTER, C.BIG_MONSTER))
GOBLIN = pygame.image.load(os.path.join("Assets", "goblin.png"))
GOBLIN = pygame.transform.scale(GOBLIN, (C.PLAYER_SIZE, C.PLAYER_SIZE))
BIG_GOBLIN = pygame.transform.scale(GOBLIN, (C.MONSTER_SIZE, C.MONSTER_SIZE))
GOLEM = pygame.image.load(os.path.join("Assets", "golem.png"))
GOLEM = pygame.transform.scale(GOLEM, (C.MONSTER_SIZE, C.MONSTER_SIZE))
HUNTER = pygame.image.load(os.path.join("Assets", "hunter.png"))
HUNTER = pygame.transform.scale(HUNTER, (C.MONSTER_SIZE, C.MONSTER_SIZE))
IMP = pygame.image.load(os.path.join("Assets", "imp.png"))
IMP = pygame.transform.scale(IMP, (C.PLAYER_SIZE, C.PLAYER_SIZE))
ORC = pygame.image.load(os.path.join("Assets", "orc.png"))
ORC = pygame.transform.scale(ORC, (C.BIG_MONSTER, C.BIG_MONSTER))
RAT = pygame.image.load(os.path.join("Assets", "Rat.png"))
RAT = pygame.transform.scale(RAT, (C.PLAYER_SIZE//2, C.PLAYER_SIZE//2))
BIG_RAT = pygame.transform.scale(RAT, (C.PLAYER_SIZE, C.PLAYER_SIZE))
GIANT_RAT = pygame.transform.scale(RAT, (C.MONSTER_SIZE, C.MONSTER_SIZE))
SERPENT = pygame.image.load(os.path.join("Assets", "Snake.png"))
SERPENT = pygame.transform.scale(SERPENT, (C.PLAYER_SIZE, C.PLAYER_SIZE))
SLIME = pygame.image.load(os.path.join("Assets", "slime.png"))
SLIME = pygame.transform.scale(SLIME, (C.MONSTER_SIZE, C.MONSTER_SIZE))
SUMMONER = pygame.image.load(os.path.join("Assets", "summoner.png"))
SUMMONER = pygame.transform.scale(SUMMONER, (C.PLAYER_SIZE, C.PLAYER_SIZE*(1.5)))
TROLL = pygame.image.load(os.path.join("Assets", "troll.png"))
TROLL = pygame.transform.scale(TROLL, (C.BIG_MONSTER, C.BIG_MONSTER))
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
        "Angel" : ANGEL, "Cave" : CAVE, "Demon" : DEMON, "Forest" : FOREST, "Goblin" : GOBLIN, "Golem" : GOLEM, "Guild" : GUILD, "Hob Goblin" : BIG_GOBLIN, "Hunter" : HUNTER, "Imp" : IMP, "Orc" : ORC, "Maid" : SUMMONER, "Map" : MAP, "Rat" : RAT, "Big Rat" : BIG_RAT, "Giant Rat" : GIANT_RAT, "Serpent" : SERPENT, "Slime" : SLIME, "Smith" : SMITH, "Summoner" : SUMMONER, "Troll" : TROLL, "Turret" : TURRET, "Vampire" : VAMPIRE, "Village" : VILLAGE, "Warrior" : WARRIOR, "Werewolf" : BEAST, "Wolf" : SMALL_BEAST
        }