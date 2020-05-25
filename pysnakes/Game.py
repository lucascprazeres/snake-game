import pygame
from time import sleep
from pysnakes.classes import Window
from pysnakes.classes.Snake import Snake

pygame.init()

class Game:
    def __init__(self):
        self.game_over = False
        self.window = None
        self.clock = pygame.time.Clock()
        self.snake = None
        # window setting
        self.screen_size = (400, 300)
        self.fps = 30
        # Game Rules
        self.boundries = {
            "x":self.screen_size[0] - 10,
            "y":self.screen_size[1] - 10
        }
        self.snake_initial_pos = (200, 150)
        self.snake_vel = 3

    def start(self):
        self.window = Window.Window(self.screen_size)
        self.snake = Snake(Window.COLORS["green"], self.snake_initial_pos)

        while not self.game_over:

            snake_hit_the_boundries = False

            if self.boundries["x"] < self.snake.pos_x or self.snake.pos_x < 0:
                snake_hit_the_boundries = True
            if self.boundries["y"] < self.snake.pos_y or self.snake.pos_y < 0:
                snake_hit_the_boundries = True

            if snake_hit_the_boundries:
                self.game_over = True

            self.game_loop()

        self.set_game_over()

    def game_loop(self):
        self.listen_to_events()
        self.snake.move()
        self.refreshScreen()
        self.drawSnake()
        pygame.display.update()
        self.clock.tick(self.fps)

    def set_game_over(self):
        self.message('Game Over!', Window.COLORS["red"])
        pygame.display.update()
        sleep(2)
        self.quit()

    def message(self, msg, color):
        font_style = pygame.font.SysFont(None, 50)
        mesg = font_style.render(msg, True, color)
        self.window.surface.blit(mesg, [self.screen_size[0]/4, self.screen_size[1]/4])

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
