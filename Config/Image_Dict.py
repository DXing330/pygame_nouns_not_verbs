import pygame

pygame.init()
import os
from Config.Constants import *
C = Constants()
WIN = pygame.display.set_mode((C.WIDTH, C.HEIGHT), pygame.RESIZABLE)
# Characters
ANGEL = pygame.image.load(os.path.join("Assets", "angel.png")).convert()
ANGEL.set_colorkey((0, 0, 0))
ANGEL = pygame.transform.scale(ANGEL, (C.PLAYER_SIZE, C.PLAYER_SIZE))
BEAST = pygame.image.load(os.path.join("Assets", "beast.png")).convert()
BEAST.set_colorkey((0, 0, 0))
BEAST = pygame.transform.scale(BEAST, (C.MONSTER_SIZE, C.MONSTER_SIZE))
SMALL_BEAST = pygame.transform.scale(BEAST, (C.PLAYER_SIZE, C.PLAYER_SIZE))
DEMON = pygame.image.load(os.path.join("Assets", "demon.png")).convert()
DEMON.set_colorkey((0, 0, 0))
DEMON = pygame.transform.scale(DEMON, (C.BIG_MONSTER, C.BIG_MONSTER))
DRAGON = pygame.image.load(os.path.join("Assets", "dragon.png")).convert()
DRAGON.set_colorkey((0, 0, 0))
DRAGON = pygame.transform.scale(DRAGON, (C.BIG_MONSTER * 1.5, C.BIG_MONSTER * 1.5))
GOBLIN = pygame.image.load(os.path.join("Assets", "goblin.png")).convert()
GOBLIN.set_colorkey((0, 0, 0))
GOBLIN = pygame.transform.scale(GOBLIN, (C.PLAYER_SIZE, C.PLAYER_SIZE))
BIG_GOBLIN = pygame.transform.scale(GOBLIN, (C.MONSTER_SIZE, C.MONSTER_SIZE))
GOLEM = pygame.image.load(os.path.join("Assets", "golem.png")).convert()
GOLEM.set_colorkey((0, 0, 0))
GOLEM = pygame.transform.scale(GOLEM, (C.MONSTER_SIZE, C.MONSTER_SIZE))
HUNTER = pygame.image.load(os.path.join("Assets", "hunter.png")).convert()
HUNTER.set_colorkey((0, 0, 0))
HUNTER = pygame.transform.scale(HUNTER, (C.MONSTER_SIZE, C.MONSTER_SIZE))
IMP = pygame.image.load(os.path.join("Assets", "imp.png")).convert()
IMP.set_colorkey((0, 0, 0))
IMP = pygame.transform.scale(IMP, (C.PLAYER_SIZE, C.PLAYER_SIZE))
ORC = pygame.image.load(os.path.join("Assets", "orc.png")).convert()
ORC.set_colorkey((0, 0, 0))
ORC = pygame.transform.scale(ORC, (C.BIG_MONSTER, C.BIG_MONSTER))
RAT = pygame.image.load(os.path.join("Assets", "Rat.png")).convert()
RAT.set_colorkey((0, 0, 0))
RAT = pygame.transform.scale(RAT, (C.PLAYER_SIZE // 2, C.PLAYER_SIZE // 2))
BIG_RAT = pygame.transform.scale(RAT, (C.PLAYER_SIZE, C.PLAYER_SIZE))
GIANT_RAT = pygame.transform.scale(RAT, (C.MONSTER_SIZE, C.MONSTER_SIZE))
SERPENT = pygame.image.load(os.path.join("Assets", "Snake.png")).convert()
SERPENT.set_colorkey((0, 0, 0))
SERPENT = pygame.transform.scale(SERPENT, (C.PLAYER_SIZE, C.PLAYER_SIZE))
SLIME = pygame.image.load(os.path.join("Assets", "slime.png")).convert()
SLIME.set_colorkey((0, 0, 0))
SLIME = pygame.transform.scale(SLIME, (C.MONSTER_SIZE, C.MONSTER_SIZE))
SUMMONER = pygame.image.load(os.path.join("Assets", "summoner.png")).convert()
SUMMONER.set_colorkey((0, 0, 0))
SUMMONER = pygame.transform.scale(SUMMONER, (C.PLAYER_SIZE, C.PLAYER_SIZE * 1.4))
TROLL = pygame.image.load(os.path.join("Assets", "troll.png")).convert()
TROLL.set_colorkey((0, 0, 0))
TROLL = pygame.transform.scale(TROLL, (C.BIG_MONSTER, C.BIG_MONSTER))
TURRET = pygame.image.load(os.path.join("Assets", "turret.png")).convert()
TURRET.set_colorkey((0, 0, 0))
TURRET = pygame.transform.scale(TURRET, (C.PLAYER_SIZE, C.PLAYER_SIZE))
VAMPIRE = pygame.image.load(os.path.join("Assets", "vampire.png")).convert()
VAMPIRE.set_colorkey((0, 0, 0))
VAMPIRE = pygame.transform.scale(VAMPIRE, (C.PLAYER_SIZE, C.PLAYER_SIZE))
WARRIOR = pygame.image.load(os.path.join("Assets", "warrior.png")).convert()
WARRIOR.set_colorkey((0, 0, 0))
WARRIOR = pygame.transform.scale(WARRIOR, (C.PLAYER_SIZE * 1.1, C.PLAYER_SIZE * 1.5))
# Backgrounds
FOREST = pygame.image.load(os.path.join("Assets", "forest1.png")).convert()
CAVE = pygame.image.load(os.path.join("Assets", "cave.png")).convert()
GUILD = pygame.image.load(os.path.join("Assets", "guild.png")).convert()
MAP = pygame.image.load(os.path.join("Assets", "map.png")).convert()
SMITH = pygame.image.load(os.path.join("Assets", "smith.png")).convert()
VILLAGE = pygame.image.load(os.path.join("Assets", "village.png")).convert()


class Image_Dict:
    def __init__(self):
        self.IMAGES = {
            "Angel": ANGEL,
            "Cave": CAVE,
            "Demon": DEMON,
            "Dragon": DRAGON,
            "Forest": FOREST,
            "Goblin": GOBLIN,
            "Golem": GOLEM,
            "Guild": GUILD,
            "Hob Goblin": BIG_GOBLIN,
            "Hunter": HUNTER,
            "Imp": IMP,
            "Orc": ORC,
            "Maid": SUMMONER,
            "Map": MAP,
            "Rat": RAT,
            "Big Rat": BIG_RAT,
            "Giant Rat": GIANT_RAT,
            "Serpent": SERPENT,
            "Slime": SLIME,
            "Smith": SMITH,
            "Summoner": SUMMONER,
            "Troll": TROLL,
            "Turret": TURRET,
            "Vampire": VAMPIRE,
            "Village": VILLAGE,
            "Warrior": WARRIOR,
            "Werewolf": BEAST,
            "Wolf": SMALL_BEAST
        }
