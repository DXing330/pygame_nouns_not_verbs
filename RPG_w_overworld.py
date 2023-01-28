import pygame
pygame.init()
import sys
sys.path.append("./Battle")
sys.path.append("./Characters")
sys.path.append("./Config")
sys.path.append("./Skills")
sys.path.append("./Utility")
sys.path.append("./Assets")
sys.path.append("./Buildings")
sys.path.append("./Maps")
from Battle.Battle_Encounter import *
from Buildings.Guildv2 import *
from Characters.Party import *
from Config.Location_Dict import *
from Maps.Battle_Zone import Battle_Zone
L = Location_Dict()
WIN = pygame.display.set_mode((C.WIDTH, C.HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()


class RPG_GAME:
    def __init__(self):
        self.party : Party = Party([], [], [])
        self.draw : Draw = Draw()
        self.player = pygame.Rect(0, 0, 50, 50)
        self.movement = 1
    
    def start_game(self):
        options = ["Continue", "New Game"]
        pick_from = Pick(options, False)
        choice = pick_from.pick()
        if choice == "New Game":
            self.party.new_party()
        elif choice == "Continue":
            self.party.load()
            self.party.party_update()
        self.game_loop()

    def update_locations(self):
        self.locations = []
        for number in range(0, self.party.journal.rank):
            new_location = Location(**L.LOCATIONS.get(number))
            self.locations.append(new_location)

    def draw_overworld(self):
        self.height = WIN.get_height()
        self.width = WIN.get_width()
        WIN.fill((0, 0, 0))
        pygame.draw.rect(WIN, (0, 150, 100), pygame.Rect(0, 0, self.width//6, self.width//6))
        pygame.draw.rect(WIN, (0, 0, 100), pygame.Rect(self.width - self.width//6, 0, self.width//6, self.width//6))
        pygame.draw.rect(WIN, (220, 200, 200), pygame.Rect(0, self.height - self.width//6, self.width//6, self.width//6))
        pygame.draw.rect(WIN, (220, 0, 0), pygame.Rect(self.width - self.width//6, self.height - self.width//6, self.width//6, self.width//6))
        pygame.draw.rect(WIN, (0, 255, 0), self.player)
        pygame.display.update()

    def game_loop(self):
        game = True
        self.update_locations()
        self.draw_overworld()
        while game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.player.x <= self.width//6 and self.player.y <= self.width//6:
                            self.party.save()
                            self.draw.draw_text("Saved")
                            pygame.time.delay(500)
                            self.draw_overworld()
                        if self.player.x <= self.width//6 and (self.player.y > self.height - self.width//6):
                            game = False
                        if (self.player.x > self.width - self.width//6) and (self.player.y > self.height - self.width//6):
                            self.party.journal.days += 1
                            self.party.pick_battle_party()
                            self.draw.draw_background("Map")
                            pick_from = Pick(self.locations, False)
                            location : Location = pick_from.pick()
                            batte_area = Battle_Zone(self.party, location)
                            batte_area.battle_loop()
                            self.draw_overworld()
                        if self.player.x > self.width - self.width//6 and self.player.y < self.width//6 - self.player.height:
                            guild = Guild(self.party)
                            guild.inside()
                            self.update_locations()
                            self.draw_overworld()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and (self.player.x) > 0:
                self.player.x -= self.movement
                self.draw_overworld()
            if keys[pygame.K_RIGHT] and (self.player.x) < (self.width - self.player.width):
                self.player.x += self.movement
                self.draw_overworld()
            if keys[pygame.K_UP] and (self.player.y) > 0:
                self.player.y -= self.movement
                self.draw_overworld()
            if keys[pygame.K_DOWN] and (self.player.y) < (self.height - self.player.height):
                self.player.y += self.movement
                self.draw_overworld()


def Play():
    RPG = RPG_GAME()
    RPG.start_game()

Play()