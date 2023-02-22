import pygame

pygame.init()


class Player_Rect:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 50, 50)
        self.move_speed = 1
        self.x_velocity = 0
        self.y_velocity = 0

    def update_dimensions(self, win_width, win_height):
        bigger_dimension = max(win_width, win_height)
        self.rect.width = bigger_dimension // 20
        self.rect.height = bigger_dimension // 20

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
                    self.rect.x = collidable.right + self.rect.width
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
        self.reset_velocity()
