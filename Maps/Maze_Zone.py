import random
import pygame
from dataclasses import dataclass
from Characters.Party import *
from Maps.Battle_Zone import *
from Maps.Player_Rect import *
from Utility.Draw import Draw
from Characters.Battle_NPC import Battle_NPC

pygame.init()

WIN = pygame.display.set_mode((1200, 700), pygame.RESIZABLE)
clock = pygame.time.Clock()


class Block:
    def __init__(self, color, rect):
        self.color = color
        self.rect: pygame.rect = rect
        self.viewable = False


class Node:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.value = 0
        self.adjacent = []
        self.shortest_path = []

    def __repr__(self):
        return str("Row: "+str(self.row)+" Column: "+str(self.column))

    def show_adjacents(self):
        return str("Adjacents: "+str(self.adjacent))
    
    
@dataclass
class Map:
    size: int = 5

    def generate_map(self):
        self.grid = [[Node(y, x) for x in range(self.size)] for y in range(self.size)]
        self.grid[self.size-1][self.size-1].value = -1
        self.turrets = [[None for number in range(self.size)] for number in range(self.size)]
        self.create_edges()

    def create_edges(self):
        for row in range(self.size):
            for column in range(self.size):
                node = self.grid[row][column]
                if row > 0:
                    node.adjacent.append(self.grid[row - 1][column])
                if row < self.size - 1:
                    node.adjacent.append(self.grid[row + 1][column])
                if column > 0:
                    node.adjacent.append(self.grid[row][column - 1])
                if column < self.size - 1:
                    node.adjacent.append(self.grid[row][column + 1])

    def place_block(self, row, column):
        self.grid[row][column].value = 1
        placable = self.check_reachability()
        if (row == 0 and column == self.size - 1) or (row == self.size - 1 and column == 0)  or (row == self.size - 1 and column == self.size - 1) or (row==column==0):
            placable = False
        if not placable:
            self.grid[row][column].value = 0

    def find_passage_nodes(self):
        # Check on all the zero or less value tiles.
        self.passable: list[Node] = []
        for x in range(self.size):
            for y in range(self.size):
                node = self.grid[x][y]
                if node.value == 0:
                    self.passable.append(node)

    def check_reachability(self):
        self.find_passage_nodes()
        self.reachable = []
        # Initialize with the ending point.
        self.reachable.append(self.grid[self.size-1][self.size-1])
        for node in self.reachable:
            self.check_reachable_nodes(node)
        if len(self.passable) <= 0:
            return True
        return False
        
    def check_reachable_nodes(self, start: Node):
        for node in start.adjacent:
            if node in self.passable:
                self.reachable.append(node)
                self.passable.remove(node)


class Maze:
    def __init__(self):
        self.map = Map(100)
        self.player = Player_Rect()
        self.block_size = 50
        self.collidables = []
        self.squares = []
        self.make_maze()

    def make_maze(self):
        self.collidables = []
        self.squares = []
        self.update_dimensions()
        self.map.generate_map()
        self.generate_blocks()
        self.make_squares()

    def update_dimensions(self):
        self.width = WIN.get_width()
        self.height = WIN.get_height()
        max_blocks = (min(self.width, self.height)//self.block_size) - 1
        self.map.size = min(self.map.size, max_blocks)
        self.player.rect.width = self.block_size//2
        self.player.rect.height = self.block_size//2
        self.total_dim = self.block_size * self.map.size
        width = (self.width - self.total_dim)//2
        height = (self.height - self.total_dim)//2
        self.player.rect.x = width
        self.player.rect.y = height

    def generate_blocks(self):
        count = self.count_blocks()
        proportion = random.gauss(2, 0.5)
        while count <= (self.map.size**2)//min(proportion, 2):
            row = random.randint(0, self.map.size-1)
            column = random.randint(0, self.map.size-1)
            self.map.place_block(row, column)
            count = self.count_blocks()

    def count_blocks(self):
        count = 0
        for row in range(self.map.size):
            for column in range(self.map.size):
                count += self.map.grid[row][column].value
        return count
    
    def make_squares(self):
        width = (self.width - self.total_dim)//2
        height = (self.height - self.total_dim)//2
        for x in range(self.map.size):
            for y in range(self.map.size):
                self.make_square(width, height, x, y)
                height += self.block_size
            height = (self.height - self.total_dim)//2
            width += self.block_size
        self.make_special_tiles()

    def make_treasure_tile(self):
        possible_treasure_locations = []
        for block in self.squares:
            if block.color == (200, 200, 200):
                possible_treasure_locations.append(block)
        self.treasure_rect = possible_treasure_locations[random.randint(0, len(possible_treasure_locations)-1)].rect

    def make_special_tiles(self):
        self.finish_rect = pygame.Rect((self.width + self.total_dim)//2 - self.block_size, (self.height + self.total_dim)//2 - self.block_size, self.block_size, self.block_size)
        self.make_treasure_tile()

    def make_square(self, width, height, x, y):
        block = Block((200, 200, 200) ,pygame.Rect(width, height, self.block_size, self.block_size))
        if self.map.grid[x][y].value > 0:
            block.color = (100, 0, 0)
            self.collidables.append(block.rect)
        self.squares.append(block)
        return block.rect
    
    def draw_special_tiles(self):
        pygame.draw.rect(WIN, (0, 100, 150), self.finish_rect)
        pygame.draw.rect(WIN, (0, 150, 100), self.treasure_rect)

    def draw_map(self):
        WIN.fill((0, 0, 0))
        for block in self.squares:
            pygame.draw.rect(WIN, block.color, block)
        self.draw_special_tiles()
        pygame.draw.rect(WIN, (0, 100, 0), self.player.rect)
        pygame.display.flip()

    def remove_player_image(self):
        pygame.draw.rect(WIN, (200, 200, 200), self.player.rect)

    def update_player_location(self):
        WIN.blit(self.player.current_sprite, (self.player.rect.x, self.player.rect.y))
        pygame.display.flip()


class Maze_Zone():
    def __init__(self, party, location):
        self.party: Party = party
        self.location: Location = location
        self.step_counter = 0
        self.counter_limit = 0
        self.found_mana = 0
        self.found_coins = 0
        self.draw = Draw()
        self.maze = Maze()
        self.maze.make_maze()
        self.treasure_limit = random.gauss(self.maze.map.size, self.maze.map.size//3)

    def determine_treasure(self):
        treasure = random.randint(0, 1)
        if treasure == 1:
            self.found_mana += random.randint(1, self.maze.map.size//3)
        elif treasure == 0:
            self.found_coins += self.maze.map.size

    def find_treasure(self):
        self.draw.draw_background()
        self.draw.draw_text("You found some treasure!")
        self.treasure_limit -= 1
        print (self.treasure_limit)
        pygame.time.delay(1000)
        self.determine_treasure()
        rect = pygame.Rect(self.maze.treasure_rect.x, self.maze.treasure_rect.y, self.maze.block_size, self.maze.block_size)
        replace_block = Block((200, 200, 200), rect)
        self.maze.squares.append(replace_block)
        self.maze.make_treasure_tile()
        self.maze.draw_map()

    def generate_battle(self, monsters = None):
        if monsters == None:
            monsters = []
        battle = Monster_Encounter(self.party, self.location, self.maze.map.size, monsters, [], [])
        battle.start_phase()

    def reset_counter(self):
        self.step_counter = 0
        self.counter_limit = random.gauss(self.maze.total_dim, self.maze.block_size)

    def check_on_party(self):
        defeated = True
        for hero in self.party.battle_party:
            if hero.health > 0:
                defeated = False
        return defeated

    def complete_maze(self):
        self.party.items.mana_crystals += self.found_mana
        self.party.items.coins += self.found_coins

    def explore_maze(self):
        self.maze.draw_map()
        self.reset_counter()
        maze = True
        while maze:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        self.party.menu(1)
                        self.maze.draw_map()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]:
                self.maze.remove_player_image()
            if keys[pygame.K_LEFT] and self.maze.player.rect.x > (self.maze.width - self.maze.total_dim)//2:
                self.maze.player.determine_movement("left", self.maze.collidables)
            if keys[pygame.K_RIGHT] and self.maze.player.rect.x < (((self.maze.width + self.maze.total_dim)//2) - self.maze.player.rect.width):
                self.maze.player.determine_movement("right", self.maze.collidables)
            if keys[pygame.K_UP] and self.maze.player.rect.y > (self.maze.height - self.maze.total_dim)//2:
                self.maze.player.determine_movement("up", self.maze.collidables)
            if keys[pygame.K_DOWN] and self.maze.player.rect.y < (((self.maze.height + self.maze.total_dim)//2) - self.maze.player.rect.height):
                self.maze.player.determine_movement("down", self.maze.collidables)
            if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]:
                self.maze.update_player_location()
                pygame.display.update()
                self.step_counter += self.maze.player.move_speed
            if self.step_counter > self.counter_limit:
                self.reset_counter()
                self.generate_battle()
                maze = not self.check_on_party()
                self.maze.draw_map()
            if self.maze.finish_rect.contains(self.maze.player.rect):
                maze = False
                self.complete_maze()
            if self.maze.treasure_rect.contains(self.maze.player.rect):
                self.find_treasure()
                if self.treasure_limit <= 0:
                    self.generate_battle(["Gold Dragon"])
                    self.treasure_limit = random.gauss(self.maze.map.size, self.maze.map.size//3)
                    maze = not self.check_on_party()
                    self.maze.draw_map()
            clock.tick(150)