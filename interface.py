import pygame
from logic import Snake, Food
from sys import exit
from tkinter import messagebox, Tk

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.snake = Snake()
        self.food = Food()
        self.clock = pygame.time.Clock()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.display.quit()
                    pygame.quit()
                    exit()

            self.clock.tick(self.snake.speed)
            self.snake.move()
            self.check_collisions()
            self.draw()

            print(running)

            # if running == False:
            #     pygame.display.quit()
            #     pygame.quit()
            #     exit()                

    def check_collisions(self):
        if self.snake.collides_with(self.food):
            self.snake.grow()
            self.food.spawn()
            self.snake.speed += 2
        if self.snake.collides_with_wall():
            root = Tk()
            root.withdraw()
            messagebox.showinfo(title=None, message="Przegrana :(")
            root.mainloop()
            self.running = False

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        pygame.display.update()