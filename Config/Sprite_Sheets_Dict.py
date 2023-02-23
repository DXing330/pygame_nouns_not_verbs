import pygame

pygame.init()
import os
WIN = pygame.display.set_mode((1200, 800), pygame.RESIZABLE)
# Characters.
PLAYER_WALK = pygame.image.load(os.path.join("Assets", "player_walk_spritesheet.png")).convert()
PLAYER_WALK.set_colorkey((0, 0, 0))


class Sprite_Sheet_Dict:
    def __init__(self):
        self.SPRITE_SHEETS = {
        "Walk" : PLAYER_WALK
        }
        self.PLAYER_SPRITE_HEIGHTS = {
        0 : 0,
        1 : 50,
        2 : 98,
        3 : 146
        }
        self.PLAYER_SPRITE_WIDTHS = {
        0 : 0,
        1 : 49,
        2 : 98
        }


class Sprite_Sheet:
    def __init__(self, name):
        self.name = name
        self.sprite_dict = Sprite_Sheet_Dict()
        self.sheet = self.sprite_dict.SPRITE_SHEETS.get(name)

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface((width, height))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sheet,(0,0),(x,y,width,height))
        return sprite


test_sprite = Sprite_Sheet("Walk")
walk_sprites = [
test_sprite.get_sprite(0, 0, 49, 50),
test_sprite.get_sprite(49, 0, 49, 50),
test_sprite.get_sprite(98, 0, 49, 50),
test_sprite.get_sprite(0, 50, 49, 48),
test_sprite.get_sprite(49, 50, 49, 48),
test_sprite.get_sprite(98, 50, 49, 48),
test_sprite.get_sprite(0, 98, 49, 48),
test_sprite.get_sprite(49, 98, 49, 48),
test_sprite.get_sprite(98, 98, 49, 48),
test_sprite.get_sprite(0, 146, 49, 54),
test_sprite.get_sprite(49, 146, 49, 54),
test_sprite.get_sprite(98, 146, 49, 54)
]

running = True
count_limit = (len(walk_sprites)//4) - 1
count = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if count > count_limit:
        count -= count_limit
    image = walk_sprites[count]
    image = pygame.transform.scale(image, (50, 50))
    image_2 = walk_sprites[count+3]
    image_2 = pygame.transform.scale(image_2, (50, 50))
    image_3 = walk_sprites[count+6]
    image_3 = pygame.transform.scale(image_3, (50, 50))
    image_4 = walk_sprites[count+9]
    image_4 = pygame.transform.scale(image_4, (50, 50))
    WIN.fill((200, 200, 200))
    WIN.blit(image, (160, 240))
    WIN.blit(image_2, (80, 160))
    WIN.blit(image_3, (240, 160))
    WIN.blit(image_4, (160, 80))
    pygame.display.update()
    pygame.time.delay(250)
    count += 1