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
from Battle.Battle_Encounter import *
from Buildings.Guildv2 import *
from Characters.Party import *
from Config.Location_Dict import *
L = Location_Dict()
from Utility.Draw import Draw
WIN = pygame.display.set_mode((C.WIDTH, C.HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()


class RPG_GAME:
    def __init__(self):
        self.party : Party = Party([], [], [])
        self.draw : Draw = Draw()
    
    def start_game(self):
        start = True
        self.draw.draw_text("New Game / Continue")
        while start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    start = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    pygame.event.clear()
                    if event.key == pygame.K_n:
                        self.party.new_party()
                        start = False
                    if event.key == pygame.K_c:
                        self.party.load()
                        self.party.party_update()
                        start = False
        self.game_loop()

    def update_locations(self):
        self.locations = []
        for number in range(0, self.party.journal.rank):
            new_location = Location(**L.LOCATIONS.get(number))
            self.locations.append(new_location)
        
    def game_loop(self):
        self.update_locations()
        game = True
        self.draw.draw_bg_and_text("Village", "Adventure / Guild / Save")
        while game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    pygame.event.clear()
                    if event.key == pygame.K_a:
                        self.party.journal.days += 1
                        self.party.pick_battle_party()
                        self.draw.draw_background("Map")
                        pick_from = Pick(self.locations, False)
                        location : Location = pick_from.pick()
                        for number in range(0, random.randint(1, location.dungeon_size)):
                            battle = Monster_Encounter(self.party, location, random.randint(1, max(number, 1)), [])
                            print (str(location.dungeon_size)+str(number)+str(location.boss))
                            if number == location.dungeon_size - 1 and location.boss:
                                print ("Found boss")
                                battle.monsters.append(location.bosses[random.randint(0, len(location.bosses) - 1)])
                                battle.boss = True
                            battle.start_phase()
                        self.draw.draw_bg_and_text("Village", "Adventure / Guild / Save")
                    if event.key == pygame.K_s:
                        self.party.save()
                        self.draw.draw_background("Village")
                        self.draw.draw_text("Saved")
                        pygame.time.delay(250)
                        self.draw.draw_bg_and_text("Village", "Adventure / Guild / Save")
                    if event.key == pygame.K_g:
                        guild = Guild(self.party)
                        guild.inside()
                        self.update_locations()
                        self.draw.draw_bg_and_text("Village", "Adventure / Guild / Save")


def Play():
    RPG = RPG_GAME()
    RPG.start_game()

Play()