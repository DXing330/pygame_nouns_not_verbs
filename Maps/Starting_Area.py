import pygame
pygame.init()
WIN = pygame.display.set_mode((1200, 800), pygame.RESIZABLE)

class Start_Zone:
    def __init__(self, party):
        self.party = party
        self.player = pygame.Rect(0, 0, 50, 50)
        self.movement = 1
        self.height = WIN.get_height()
        self.width = WIN.get_width()

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

    def loop(self):
        game = True
        self.draw_overworld()
        while game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.player.x <= self.width//6 and self.player.y <= self.width//6:
                            print ("Saved")
                        if self.player.x <= self.width//6 and (self.player.y > self.height - self.width//6):
                            game = False
                        if (self.player.x > self.width - self.width//6) and (self.player.y > self.height - self.width//6):
                            print ("Battle")
                        if self.player.x > self.width - self.width//6 and self.player.y < self.width//6 - self.player.height:
                            print ("Guild")
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

start = Start_Zone(None)
start.loop()