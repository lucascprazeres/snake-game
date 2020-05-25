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
        self.screen_size = (400, 300)
        self.boundries = {
            "x":self.screen_size[0] - 15,
            "y":self.screen_size[1] - 15
        }
        self.snake_initial_pos = (200, 150)
        self.snake_vel = 5

    def start(self):
        self.window = Window.Window(self.screen_size)
        self.snake = Snake(Window.COLORS["green"], self.snake_initial_pos)

        while not self.game_over:
            snake_hit_the_boundries = False

            if self.boundries["x"] < self.snake.pos_x or self.snake.pos_x < 5:
                snake_hit_the_boundries = True
            if self.boundries["y"] < self.snake.pos_y or self.snake.pos_y < 5:
                snake_hit_the_boundries = True

            self.listen_to_events()
            self.snake.move()
            self.refreshScreen()
            self.drawSnake()
            pygame.display.update()
            self.clock.tick(30)

            print(snake_hit_the_boundries)

            if snake_hit_the_boundries:
                self.game_over = True

        self.quit()

    def refreshScreen(self):
        self.window.surface.fill(Window.COLORS["black"])

    def drawSnake(self):
        surface = self.window.surface
        color = self.snake.color
        pos = (self.snake.pos_x, self.snake.pos_y)
        size = self.snake.size

        pygame.draw.rect(surface, color, [*pos, *size])


    def listen_to_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction(0, -self.snake_vel)
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction(0, self.snake_vel)
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction(self.snake_vel, 0)
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction(-self.snake_vel, 0)


    def quit(self):
        self.window.close()
