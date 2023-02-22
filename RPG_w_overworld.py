import pygame
pygame.init()


from Buildings.Guildv2 import *
from Config.Location_Dict import *
from Maps.Labyrinth_Zone import *

L = Location_Dict()
WIN = pygame.display.set_mode((C.WIDTH, C.HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()


class RPG_GAME:
    def __init__(self):
        self.party: Party = Party([], [], [])
        self.draw: Draw = Draw()
        self.player = Player_Rect()
        self.width = C.WIDTH
        self.height = C.HEIGHT
        self.battle_rect = pygame.Rect(self.width - self.width // 6, self.height - self.width // 6, self.width // 6,
                                       self.width // 6)
        self.guild_rect = pygame.Rect(self.width - self.width // 6, 0, self.width // 6, self.width // 6)
        self.locations = []
        self.game = True

    def start_game(self):
        self.draw.draw_background()
        options = ["Continue", "New Game", "Quit"]
        pick_from = Pick(options, False)
        choice = pick_from.pick()
        if choice == "New Game":
            self.party.new_party()
        elif choice == "Continue":
            try:
                self.party.load()
            except:
                self.draw.draw_background()
                self.draw.draw_text("No Saved Data")
                pygame.time.delay(500)
                self.start_game()
        elif choice == "Quit":
            pygame.quit()
            self.game = False
        self.game_loop()

    def update_locations(self):
        locations = []
        for location_name in self.party.locations:
            loc_dict = L.LOCATIONS_NAMES.get(location_name)
            if loc_dict is not None:
                new_location = Location(**loc_dict)
                locations.append(new_location)
        self.locations = locations

    def update_dimensions(self):
        self.height = WIN.get_height()
        self.width = WIN.get_width()
        self.battle_rect = pygame.Rect(self.width - self.width // 8, self.height - self.width // 8, self.width // 8,
                                       self.width // 8)
        self.guild_rect = pygame.Rect(self.width - self.width // 8, 0, self.width // 8, self.width // 8)
        self.player.update_dimensions(WIN.get_width(), WIN.get_height())

    def draw_overworld(self):
        WIN.fill((0, 0, 0))
        pygame.draw.rect(WIN, (0, 0, 100), self.guild_rect)
        pygame.draw.rect(WIN, (220, 0, 0), self.battle_rect)
        pygame.draw.rect(WIN, (0, 255, 0), self.player.rect)
        pygame.display.update()

    def game_loop(self):
        if self.game:
            self.update_locations()
            self.draw_overworld()
            self.party.initialize_battle_party(1)
        while self.game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        choice = self.party.menu()
                        if choice == "STOP":
                            self.start_game()
                        self.draw_overworld()
                    if event.key == pygame.K_SPACE:
                        if self.battle_rect.contains(self.player.rect):
                            self.draw.draw_background("Map")
                            pick_from = Pick(self.locations, False)
                            location = pick_from.pick()
                            if location.name == "Town":
                                pass
                            else:
                                self.party.journal.days += 1
                                battle_area = Labyrinth(self.party, location)
                                battle_area.generate_labyrinth()
                                battle_area.lab_loop()
                                self.party.check_quest_completion()
                            self.party.check_on_battle_party()
                            self.draw_overworld()
                        if self.guild_rect.contains(self.player.rect):
                            guild = Guild(self.party)
                            guild.inside()
                            self.update_locations()
                            self.draw_overworld()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and self.player.rect.x > 2:
                self.player.determine_movement("left")
            if keys[pygame.K_RIGHT] and self.player.rect.x < (self.width - self.player.rect.width):
                self.player.determine_movement("right")
            if keys[pygame.K_UP] and self.player.rect.y > 2:
                self.player.determine_movement("up")
            if keys[pygame.K_DOWN] and self.player.rect.y < (self.height - self.player.rect.height):
                self.player.determine_movement("down")
            if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]:
                self.draw_overworld()


def Play():
    RPG = RPG_GAME()
    RPG.start_game()


Play()
