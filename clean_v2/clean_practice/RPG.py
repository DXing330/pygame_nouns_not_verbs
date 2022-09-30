import pygame
pygame.init()
import sys
sys.path.append("./Battle")
sys.path.append("./Characters")
sys.path.append("./Config")
sys.path.append("./Skills")
sys.path.append("./Utility")
from Battle.Battle_Encounter import *
WIN = pygame.display.set_mode((C.WIDTH, C.HEIGHT), pygame.RESIZABLE)
