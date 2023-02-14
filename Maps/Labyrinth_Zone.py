from Battle.Location import Location
from Battle_Zone import *
from Characters.Party import *
from Utility.Draw import Draw


class Labyrinth(Battle_Zone):
    def __init__(self, party, location):
        self.party: Party = party
        self.location: Location = location
        # How big each floor is.
        self.floor_size = min(max(3, self.location.dungeon_size), 6)
        # How many floors there are total.
        self.total_floors = max(3, self.location.dungeon_size)
        self.counter = 0
        self.counter_limit = 0
        self.movement = 1
        self.height = WIN.get_height()
        self.width = WIN.get_width()
        self.player = pygame.Rect(0, 0, self.width//20, self.width//20)
        # Keep track of what floor you're on.
        self.floor = 0

    def update_dimensions(self):
        self.height = WIN.get_height()
        self.width = WIN.get_width()
        self.player = pygame.Rect(self.width//2, self.height//2, self.width//20, self.width//20)

    def generate_labyrinth(self):
        self.floors = [[0 for number in range(self.floor_size)] for number in range(self.total_floors)]
        self.floors_status = [[False for number in range(self.floor_size)] for number in range(self.total_floors)]
        self.generate_next_floor_passage()
        self.generate_loop_passages()
        self.generate_previous_floor_passage()
        self.decide_possible_passages()

    def pick_unused_passage(self, floor):
        possible_passages = []
        for index in range(len(self.floors[floor])):
            if self.floors[floor][index] == 0:
                possible_passages.append(index)
        picked_passage = possible_passages[random.randint(0, len(possible_passages)-1)]
        return picked_passage

    def generate_next_floor_passage(self):
        for number in range(self.total_floors):
            next = random.randint(0, self.floor_size-1)
            if number < self.total_floors - 1:
                # Go up to the next floor.
                self.floors[number][next] = number + 1
            elif number == self.total_floors - 1:
                # -1 indicates exit.
                self.floors[number][next] = -1

    def generate_previous_floor_passage(self):
        for number in range(self.total_floors):
            if number > 0:
                for index in range(self.floor_size):
                    if self.floors[number][index] == 0:
                        self.floors[number][index] = number -1

    def generate_loop_passages(self):
        for floor in range(self.total_floors):
            if floor > 0:
                passage = self.pick_unused_passage(floor)
                self.floors[floor][passage] = floor

    def decide_possible_passages(self):
        self.possible_passages = []
        self.update_dimensions()
        self.passage_0 = pygame.Rect((self.width - self.width//8)//2, 0, self.width//8, self.width//8)
        self.passage_1 = pygame.Rect(0, self.height - self.width//8, self.width//8, self.width//8)
        self.passage_2 = pygame.Rect(self.width - self.width//8, self.height - self.width//8, self.width//8, self.width//8)
        self.passage_3 = pygame.Rect((self.width - self.width//8)//2, self.height - self.width//8, self.width//8, self.width//8)
        self.passage_4 = pygame.Rect(0, 0, self.width//8, self.width//8)
        self.passage_5 = pygame.Rect(self.width - self.width//8, 0, self.width//8, self.width//8)
        self.possible_passages.append(self.passage_0)
        self.possible_passages.append(self.passage_1)
        if self.floor_size >= 3:
            self.possible_passages.append(self.passage_2)
        if self.floor_size >= 4:
            self.possible_passages.append(self.passage_3)
        if self.floor_size >= 5:
            self.possible_passages.append(self.passage_4)
        if self.floor_size >= 6:
            self.possible_passages.append(self.passage_5)

    def draw_passages(self):
        WIN.fill((0, 0, 0))
        for passage in self.possible_passages:
            color = (100, 100, 100)
            # Keep track of which passages have already been used.
            if self.floors_status[self.floor][self.possible_passages.index(passage)]:
                if self.floors[self.floor][self.possible_passages.index(passage)] == self.floor:
                    color = (100, 100, 200)
                elif self.floors[self.floor][self.possible_passages.index(passage)] > self.floor:
                    color = (100, 200, 100)
                elif self.floors[self.floor][self.possible_passages.index(passage)] < self.floor:
                    color = (200, 100, 100)
            pygame.draw.rect(WIN, color, passage)
        pygame.draw.rect(WIN, (0, 255, 0), self.player)
        pygame.display.update()

    def track_passages(self, passage):
        self.floors_status[self.floor][passage] = True

    def change_floor(self, passage: int):
        # Move to whichever floor the passage that you chose goes through.
        self.track_passages(passage)
        if self.floors[self.floor][passage] == -1:
            self.lab = False
            self.finished_lab()
        if self.lab:
            self.floor = self.floors[self.floor][passage]
            self.player.x = (self.width)//2
            self.player.y = (self.height)//2
            pygame.event.clear()
            self.draw_passages()

    def finished_lab(self):
        self.party.items.coins += self.total_floors * (self.floor_size//2)
        for quest in self.party.quests:
            if quest.requirement == "Clear" and quest.location == self.location.name:
                quest.completed = True
            if quest.requirement == "Save" and quest.location == self.location.name:
                for hero in self.party.battle_party:
                    if hero.name == quest.specifics:
                        quest.completed = True
                        self.party.battle_party.remove(hero)

    def lab_loop(self):
        self.lab = True
        print (self.floors)
        self.draw_passages()
        self.determine_weather()
        self.reset_counter()
        while self.lab:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        self.party.menu()
                        self.draw_passages()
                    if event.key == pygame.K_SPACE:
                        pygame.event.clear()
                        passage = None
                        if self.passage_0.contains(self.player):
                            passage = 0
                        if self.passage_1.contains(self.player):
                            passage = 1
                        if self.passage_2.contains(self.player):
                            passage = 2
                        if self.passage_3.contains(self.player):
                            passage = 3
                        if self.passage_4.contains(self.player):
                            passage = 4
                        if self.passage_5.contains(self.player):
                            passage = 5
                        if passage != None:
                            self.change_floor(passage)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and (self.player.x) > 0:
                self.player.x -= self.movement
                self.counter += self.movement
                self.draw_passages()
            if keys[pygame.K_RIGHT] and (self.player.x) < (self.width - self.player.width):
                self.player.x += self.movement
                self.counter += self.movement
                self.draw_passages()
            if keys[pygame.K_UP] and (self.player.y) > 0:
                self.player.y -= self.movement
                self.counter += self.movement
                self.draw_passages()
            if keys[pygame.K_DOWN] and (self.player.y) < (self.height - self.player.height):
                self.player.y += self.movement
                self.counter += self.movement
                self.draw_passages()
            if self.counter >= self.counter_limit:
                self.reset_counter()
                battle = Monster_Encounter(self.party, self.location, random.randint(1, self.location.dungeon_size), [], [], [self.weather])
                if self.location.boss and battle.amount == self.location.dungeon_size:
                    battle.boss = True
                battle.start_phase()
                self.draw_passages()
                self.lab = not self.check_on_party()