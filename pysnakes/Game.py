import pygame
from pysnakes.classes import Window
from pysnakes.classes.Snake import Snake

class Game:
    def __init__(self):
        self.game_over = False
        self.window = None
        self.clock = pygame.time.Clock()
        self.snake = None
        # Game Rules
        self.snake_initial_pos = (200, 150)
        self.snake_vel = 5

    def start(self):
        self.window = Window.Window((400, 300))
        self.snake = Snake(Window.COLORS["green"], self.snake_initial_pos)

        while not self.game_over:
            self.listen_to_events()
            self.snake.move()
            self.refreshScreen()
            self.drawSnake()
            pygame.display.update()
            self.clock.tick(30)

    def refreshScreen(self):
        self.window.surface.fill(Window.COLORS["black"])

    def drawSnake(self):
        surface = self.window.surface
        color = self.snake.color
        pos = (self.snake.pos_x, self.snake.pos_y)
        size = self.snake.size

        print(surface, color, pos, size)

        pygame.draw.rect(surface, color, [*pos, *size])


    def listen_to_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.handle_quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction(0, -self.snake_vel)
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction(0, self.snake_vel)
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction(self.snake_vel, 0)
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction(-self.snake_vel, 0)


    def handle_quit(self):
        self.window.close()
