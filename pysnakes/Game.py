import pygame
from pysnakes.classes import Window
from pysnakes.classes.Snake import Snake

class Game:
    def __init__(self):
        self.game_over = False
        self.window = None
        self.snake = None
        self.snake_initial_pos = (200, 150)

    def start(self):
        self.window = Window.Window((400, 300))
        self.snake = Snake(Window.COLORS["green"], self.snake_initial_pos)

        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.window.close()
            self.drawSnake()
            pygame.display.update()

    def drawSnake(self):
        surface = self.window.surface
        color = self.snake.color
        initial_pos = self.snake_initial_pos
        size = self.snake.size

        pygame.draw.rect(surface, color, [*initial_pos, *size])