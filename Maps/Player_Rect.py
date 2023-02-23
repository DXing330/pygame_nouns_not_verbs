import pygame
import os
pygame.init()
WIN = pygame.display.set_mode((1200, 800), pygame.RESIZABLE)
PLAYER_WALK = pygame.image.load(os.path.join("Assets", "player_walk_spritesheet.png")).convert()
PLAYER_WALK.set_colorkey((0, 0, 0))


class Sprite_Sheet:
    def __init__(self, sheet):
        self.sheet = sheet

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface((width, height))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sheet,(0,0),(x,y,width,height))
        return sprite
    
    def generate_walk_sprites(self):
        walk_sprites = [
        self.get_sprite(0, 0, 49, 50),
        self.get_sprite(49, 0, 49, 50),
        self.get_sprite(98, 0, 49, 50),
        self.get_sprite(0, 50, 49, 48),
        self.get_sprite(49, 50, 49, 48),
        self.get_sprite(98, 50, 49, 48),
        self.get_sprite(0, 98, 49, 48),
        self.get_sprite(49, 98, 49, 48),
        self.get_sprite(98, 98, 49, 48),
        self.get_sprite(0, 146, 49, 54),
        self.get_sprite(49, 146, 49, 54),
        self.get_sprite(98, 146, 49, 54)
        ]
        return walk_sprites


class Player_Rect:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 50, 50)
        self.sprite_sheet = Sprite_Sheet(PLAYER_WALK)
        self.move_speed = 50
        self.x_velocity = 0
        self.y_velocity = 0
        self.walk_sprites = self.sprite_sheet.generate_walk_sprites()
        self.current_sprite = self.walk_sprites[1]

    def update_dimensions(self, win_width, win_height):
        smaller_dimension = min(win_width, win_height)
        self.rect.width = smaller_dimension // 20
        self.rect.height = smaller_dimension // 20
        self.move_speed = self.rect.width
        for sprite in self.walk_sprites:
            sprite = pygame.transform.scale(sprite, (self.rect.width, self.rect.height))

    def determine_sprite(self):
        if self.y_velocity > 0:
            if self.current_sprite == self.walk_sprites[1]:
                self.current_sprite = self.walk_sprites[2]
            elif self.current_sprite == self.walk_sprites[2]:
                self.current_sprite = self.walk_sprites[0]
            else:
                self.current_sprite = self.walk_sprites[1]
        elif self.y_velocity < 0:
            if self.current_sprite == self.walk_sprites[10]:
                self.current_sprite = self.walk_sprites[11]
            elif self.current_sprite == self.walk_sprites[11]:
                self.current_sprite = self.walk_sprites[9]
            else:
                self.current_sprite = self.walk_sprites[10]
        if self.x_velocity > 0:
            if self.current_sprite == self.walk_sprites[7]:
                self.current_sprite = self.walk_sprites[8]
            elif self.current_sprite == self.walk_sprites[8]:
                self.current_sprite = self.walk_sprites[6]
            else:
                self.current_sprite = self.walk_sprites[7]
        elif self.x_velocity < 0:
            if self.current_sprite == self.walk_sprites[4]:
                self.current_sprite = self.walk_sprites[5]
            elif self.current_sprite == self.walk_sprites[5]:
                self.current_sprite = self.walk_sprites[3]
            else:
                self.current_sprite = self.walk_sprites[4]

    def reset_velocity(self):
        self.x_velocity = 0
        self.y_velocity = 0

    def determine_collisions(self, collidables=None):
        if collidables is None:
            collidables = []
        for collidable in collidables:
            if self.rect.colliderect(collidable):
                if self.x_velocity > 0:
                    self.rect.x = collidable.left - self.rect.width
                elif self.x_velocity < 0:
                    self.rect.x = collidable.right
                if self.y_velocity > 0:
                    self.rect.y = collidable.top - self.rect.height
                elif self.y_velocity < 0:
                    self.rect.y = collidable.bottom

    def determine_movement(self, direction, collidables=None):
        if collidables is None:
            collidables = []
        if direction == "left":
            self.x_velocity -= self.move_speed
        if direction == "right":
            self.x_velocity += self.move_speed
        if direction == "up":
            self.y_velocity -= self.move_speed
        if direction == "down":
            self.y_velocity += self.move_speed
        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity
        self.determine_collisions(collidables)
        self.determine_sprite()
        self.reset_velocity()
