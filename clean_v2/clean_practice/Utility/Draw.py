import pygame
pygame.init()
from Config.Constants import Constants
C = Constants()
clock = pygame.time.Clock()
FONT = pygame.font.SysFont("comicsans", C.REG_FONT)
WIN = pygame.display.set_mode((C.WIDTH, C.HEIGHT), pygame.RESIZABLE)

class Draw:
    def __init__(self):
        self.width = WIN.get_width()
        self.height = WIN.get_height()