import pygame
from pysnakes.classes import Window
from pysnakes.classes.Snake import Snake
from pysnakes.classes.Apple import Apple

pygame.init()

class Game:
    def __init__(self):
        self.game_is_paused = False
        self.game_over = False
        self.score = 0
        self.clock = pygame.time.Clock()
        # window setting
        self.screen_size = (400, 300)
        self.fps = 15
        # Game Rules
        self.boundries = {
            "x":self.screen_size[0] - 10,
            "y":self.screen_size[1] - 10
        }
        self.snake_block = 10
        self.snake_initial_pos = (200, 150)
        self.snake_vel = 10

    def start(self):
        self.window = Window.Window(self.screen_size)
        self.create_snake()
        self.create_apple()

        while not self.game_over:
            while self.game_is_paused:
                self.refreshScreen()
                self.message("You Lost! Press Q to quit or C to play again", Window.COLORS["red"])
                self.listen_to_events()
            self.gameLoop()

    def restart(self):
        self.score = 0
        self.create_snake()
        self.create_apple()
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
        self.drawn_apple()
        self.update_snake_coordinates()

        if self.snake_hits_itself():
            self.game_is_paused = True

        self.draw_snake()
        self.display_score()

        if self.snake.pos_x == self.apple.pos_x and self.snake.pos_y == self.apple.pos_y:
            self.create_apple()
            self.score += 1
            self.snake.length += 1

        pygame.display.update()

        self.clock.tick(self.fps)

    def display_score(self):
        score_font = pygame.font.SysFont("comicsansms", 35)
        value = score_font.render("Your Score: " + str(self.score), True, Window.COLORS["blue"])
        self.window.surface.blit(value, [0, 0])


    def message(self, msg, color):
        font_style = pygame.font.SysFont("bahnschrift", 25)
        mesg = font_style.render(msg, True, color)
        self.window.surface.blit(mesg, [20, 100])
        pygame.display.update()

    def refreshScreen(self):
        self.window.surface.fill(Window.COLORS["black"])

    def create_snake(self):
        self.snake = Snake(Window.COLORS["green"], self.snake_initial_pos, self.snake_block)

    def update_snake_coordinates(self):
        self.snake.head = []
        self.snake.head.append(self.snake.pos_x)
        self.snake.head.append(self.snake.pos_y)
        self.snake.body.append(self.snake.head)
        if len(self.snake.body) > self.snake.length:
            del self.snake.body[0]

    def snake_hits_itself(self):
        for block in self.snake.body[:-1]:
            if block == self.snake.head:
                return True
        return False

    def draw_snake(self):
        surface = self.window.surface
        color = self.snake.color
        area_per_block = (self.snake.block, self.snake.block)

        for block in self.snake.body:
            pygame.draw.rect(surface, color, [block[0], block[1], *area_per_block])



    def create_apple(self):
        self.apple = Apple(self.screen_size[0], self.screen_size[1], self.snake.block, Window.COLORS["red"])

    def drawn_apple(self):
        surface = self.window.surface
        pos = (self.apple.pos_x, self.apple.pos_y)
        block = self.apple.block
        color =self.apple.color

        pygame.draw.rect(surface, color, [*pos, block, block])


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
