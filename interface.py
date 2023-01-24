from colors import pink, red
from data import Score
from logic import Food, Snake
import pygame

class SnakeGame:

    def __init__(self):
        pygame.init()
        self.screen_width = 600
        self.screen_height = 400
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.screen.fill(pink)
        pygame.display.set_caption("Snake by A. Hinc, V. Melnik, Z. Gąsienica-Samek")
        self.font = pygame.font.SysFont("Lucida Console", 20)
        self.snake = Snake()
        self.food = Food()
        self.score = Score()
        self.clock = pygame.time.Clock()
        self.game_over = False
        self.game_close = False

    def run(self):
        while not self.game_over:

            while self.game_close:
                self.screen.fill(pink)
                self.display_score()
                self.display_highscore()
                self.message("Przegrana! R - restart, Esc - wyjście", red)
                pygame.display.update()

                for event in pygame.event.get():
                    self.restart_or_quit(event)

            for event in pygame.event.get():
                self.restart_or_quit(event)
                self.snake.change_direction(event)

            self.clock.tick(self.snake.speed)
            self.snake.move()
            self.check_collisions()
            self.draw()
            self.score.update_highscore()

        pygame.quit()
        quit()   

    def message(self, text, color):
        text = self.font.render(text, True, color)
        text_rect = text.get_rect(center = (self.screen_width / 2, self.screen_height / 2))
        self.screen.blit(text, text_rect)

    def display_score(self):
        text = self.font.render("Wynik: " + str(self.score.value), True, red)
        self.screen.blit(text, [25, 10])

    def display_highscore(self):
        text = self.font.render("Rekord: " + str(self.score.highscore), True, red)
        self.screen.blit(text, [self.screen_width - 150, 10])

    def check_collisions(self):
        if self.snake.collides_with_food(self.food):
            self.snake.grow()
            self.food.spawn(self.screen_width, self.screen_height, self.snake.body)
            self.score.value += 1
            self.snake.speed += 1
        if self.snake.collides_with_wall(self.screen_width, self.screen_height) or self.snake.collides_with_itself():
            self.game_close = True

    def draw(self):
        self.screen.fill(pink)
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        self.display_score()
        self.display_highscore()
        pygame.display.update()
    
    @staticmethod
    def start(first_game):
        game = SnakeGame()
        if first_game:
            game.message("R - restart, Esc - wyjście", red)
            pygame.display.update()
            pygame.time.delay(1500)
        game.run()
    
    def restart_or_quit(self, event):
        if event.type == pygame.QUIT:
            self.game_over = True
            self.game_close = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                self.start(False)
            if event.key == pygame.K_ESCAPE:
                self.game_over = True
                self.game_close = False