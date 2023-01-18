from random import randint
import pygame

class Snake:
    def __init__(self):
        self.body = [(200, 200), (210, 200), (220, 200)]
        self.direction = (10, 0)
        self.speed = 5

    def move(self):
        x, y = self.body[0]
        x += self.direction[0]
        y += self.direction[1]

        # To chyba trzeba przenieść
        for event in pygame.event.get():
            # if event.type == pygame.QUIT:
            #         pygame.display.quit()
            #         pygame.quit()
            #         exit()

            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_UP or event.key == pygame.K_w) and self.direction != (0, 10):
                    self.direction = (0, -10)
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and self.direction != (10, 0):
                    self.direction = (-10, 0)
                if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and self.direction != (0, -10):
                    self.direction = (0, 10)
                if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and self.direction != (-10, 0):
                    self.direction = (10, 0)
        
        self.body.insert(0, (x, y))
        self.body.pop()
        
    def collides_with(self, food):
        return self.body[0] == food.position
    
    def collides_with_wall(self):
        window_width = 800
        window_height = 600
        x, y = self.body[0]
        if x >= window_width or x < 0 or y >= window_height or y < 0:
            return True

    def grow(self):
        x, y = self.body[-1]
        self.body.append((x, y))

    def draw(self, surface):
        for x, y in self.body:
            pygame.draw.rect(surface, (255, 255, 255), (x, y, 10, 10))

class Food:
    def __init__(self):
        self.position = (300, 300)

    def spawn(self):
        self.position = (randint(0, 79) * 10, randint(0, 59) * 10)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), (self.position[0], self.position[1], 10, 10))