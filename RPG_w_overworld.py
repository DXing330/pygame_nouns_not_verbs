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
from Maps.Labyrinth_Zone import *
L = Location_Dict()
WIN = pygame.display.set_mode((C.WIDTH, C.HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()


class RPG_GAME:
    def __init__(self):
        self.party : Party = Party([], [], [])
        self.draw : Draw = Draw()
        self.player = pygame.Rect(0, 0, 50, 50)
        self.movement = 2
        self.game = True
    
    def start_game(self):
        options = ["Continue", "New Game", "Quit"]
        pick_from = Pick(options, False)
        choice = pick_from.pick()
        if choice == "New Game":
            self.party.new_party()
        elif choice == "Continue":
            try:
                self.party.load()
                self.party.party_update()
            except:
                self.start_game()
        elif choice == "Quit":
            pygame.quit()
            self.game = False
        self.game_loop()

    def update_locations(self):
        self.locations = []
        for location_name in self.party.locations:
            loc_dict = L.LOCATIONS_NAMES.get(location_name)
            if loc_dict != None:
                new_location = Location(**loc_dict)
                self.locations.append(new_location)

    def draw_overworld(self):
        self.height = WIN.get_height()
        self.width = WIN.get_width()
        WIN.fill((0, 0, 0))
        self.save_rect = pygame.Rect(0, 0, self.width//6, self.width//6)
        self.quit_rect = pygame.Rect(0, self.height - self.width//6, self.width//6, self.width//6)
        self.guild_rect = pygame.Rect(self.width - self.width//6, 0, self.width//6, self.width//6)
        self.battle_rect = pygame.Rect(self.width - self.width//6, self.height - self.width//6, self.width//6, self.width//6)
        pygame.draw.rect(WIN, (0, 150, 100), self.save_rect)
        pygame.draw.rect(WIN, (0, 0, 100), self.guild_rect)
        pygame.draw.rect(WIN, (220, 200, 200), self.quit_rect)
        pygame.draw.rect(WIN, (220, 0, 0), self.battle_rect)
        pygame.draw.rect(WIN, (0, 255, 0), self.player)
        pygame.display.update()

    def game_loop(self):
        if self.game:
            self.update_locations()
            self.draw_overworld()
            self.party.initialize_battle_party()
        while self.game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        self.party.menu()
                        self.draw_overworld()
                    if event.key == pygame.K_SPACE:
                        if self.save_rect.contains(self.player):
                            self.party.save()
                            self.draw.draw_text("Saved")
                            pygame.time.delay(500)
                            self.draw_overworld()
                        if self.quit_rect.contains(self.player):
                            self.game = False
                        if self.battle_rect.contains(self.player):
                            self.party.journal.days += 1
                            self.draw.draw_background("Map")
                            pick_from = Pick(self.locations, False)
                            location = pick_from.pick()
                            if location.name == "Town":
                                pass
                            else:
                                battle_area = Labyrinth(self.party, location)
                                battle_area.generate_labyrinth()
                                battle_area.lab_loop()
                                self.party.check_quest_completion()
                            self.draw_overworld()
                        if self.guild_rect.contains(self.player):
                            guild = Guild(self.party)
                            guild.inside()
                            self.update_locations()
                            self.draw_overworld()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and (self.player.x) > 2:
                self.player.x -= self.movement
                self.draw_overworld()
            if keys[pygame.K_RIGHT] and (self.player.x) < (self.width - self.player.width):
                self.player.x += self.movement
                self.draw_overworld()
            if keys[pygame.K_UP] and (self.player.y) > 2:
                self.player.y -= self.movement
                self.draw_overworld()
            if keys[pygame.K_DOWN] and (self.player.y) < (self.height - self.player.height):
                self.player.y += self.movement
                self.draw_overworld()


def Play():
    RPG = RPG_GAME()
    RPG.start_game()

Play()