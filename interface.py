import pygame
from logic import Snake, Food
from sys import exit
from tkinter import messagebox, Tk, Button

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.snake = Snake()
        self.food = Food()
        self.clock = pygame.time.Clock()
        
    running = True

    def run(self):
        #running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    #pygame.display.quit()
                    #pygame.quit()
                    #exit()
                self.snake.change_direction(event)

            self.clock.tick(self.snake.speed)
            self.snake.move()
            self.check_collisions()
            self.draw()



            #for event in pygame.event.get():
            # if event.type == pygame.QUIT:
            #         pygame.display.quit()
            #         pygame.quit()
            #         exit()

        event = pygame.event.get()     
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            exit()                

    root = Tk()

    def check_collisions(self):
        if self.snake.collides_with(self.food):
            self.snake.grow()
            self.food.spawn()
            self.snake.speed += 2
        if self.snake.collides_with_wall():
            #root = Tk()
            #messagebox.showinfo(title=None, message="Przegrana :(")
            close_button = Button(self.root, text = "Zamknij", command = self.close_window)
            close_button.pack()
            #self.root.withdraw()
            #self.root.after(1000, self.close_game)
            self.root.mainloop()
            self.running = False

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        pygame.display.update()
    
    def close_window(self):
        #if messagebox.askokcancel("Komunikat", "Czy na pewno chcesz zamknąć okno?"):
        self.root.destroy()
    #     #pygame.quit()