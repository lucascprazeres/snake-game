import pygame
from pysnakes.classes import Window
from pysnakes.classes.Snake import Snake

pygame.init()

class Game:
    def __init__(self):
        self.game_is_paused = False
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
            while self.game_is_paused:
                self.refreshScreen()
                self.message("You Lost! Press Q to quit or C to play again", Window.COLORS["red"])
                self.listen_to_events()
            self.gameLoop()

    def restart(self):
        self.snake = Snake(Window.COLORS["green"], self.snake_initial_pos)
        self.gameLoop()

    def gameLoop(self):

        snake_hit_the_boundries = False

        if self.boundries["x"] < self.snake.pos_x or self.snake.pos_x < 0:
            snake_hit_the_boundries = True
        if self.boundries["y"] < self.snake.pos_y or self.snake.pos_y < 0:
            snake_hit_the_boundries = True

        if snake_hit_the_boundries:
            self.game_is_paused = True
            return

        self.listen_to_events()
        self.snake.move()
        self.refreshScreen()
        self.drawSnake()
        self.clock.tick(self.fps)

    def message(self, msg, color):
        font_style = pygame.font.SysFont(None, 25)
        mesg = font_style.render(msg, True, color)
        self.window.surface.blit(mesg, [20, 100])
        pygame.display.update()

    def refreshScreen(self):
        self.window.surface.fill(Window.COLORS["black"])

    def drawSnake(self):
        surface = self.window.surface
        color = self.snake.color
        pos = (self.snake.pos_x, self.snake.pos_y)
        size = self.snake.size

        pygame.draw.rect(surface, color, [*pos, *size])
        pygame.display.update()


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
            #unlocks it when the game is paused
            if self.game_is_paused:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.game_over = True
                        self.game_is_paused = False
                    if event.key == pygame.K_c:
                        self.game_is_paused = False
                        self.restart()

    def quit(self):
        self.window.close()
