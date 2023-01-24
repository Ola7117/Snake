from colors import red, white
import pygame
from random import randint

class Snake:

    def __init__(self):
        self.body = [(220, 200), (210, 200), (200, 200)]
        self.direction = (10, 0)
        self.speed = 10

    def move(self):
        x, y = self.body[0]
        x += self.direction[0]
        y += self.direction[1]
        self.body.insert(0, (x, y))
        self.body.pop()
    
    def change_direction(self, event):
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP or event.key == pygame.K_w) and self.direction != (0, 10):
                self.direction = (0, -10)
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and self.direction != (10, 0):
                self.direction = (-10, 0)
            if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and self.direction != (0, -10):
                self.direction = (0, 10)
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and self.direction != (-10, 0):
                self.direction = (10, 0)
        
    def collides_with_food(self, food):
        return self.body[0] == food.position
    
    def collides_with_wall(self, screen_width, screen_height):
        x, y = self.body[0]
        if x >= screen_width or x < 0 or y >= screen_height or y < 0:
            return True

    def collides_with_itself(self):
        for i in self.body[1:]:
            if i == self.body[0]:
                return True
        return False

    def grow(self):
        x, y = self.body[-1]
        self.body.append((x, y))

    def draw(self, surface):
        for x, y in self.body:
            pygame.draw.rect(surface, white, (x, y, 10, 10))

class Food:

    def __init__(self):
        self.position = (400, 300)

    def spawn(self, screen_width, screen_height, snake_body):
        new_position = snake_body[0]
        while new_position in snake_body:
            new_position = (randint(0, screen_width / 10 - 1) * 10, randint(0, screen_height / 10 - 1) * 10)
        self.position = new_position

    def draw(self, screen):
        pygame.draw.rect(screen, red, (self.position[0], self.position[1], 10, 10))