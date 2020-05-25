import pygame
from pysnakes.classes.Window import Window

class Game:
    def __init__(self):
        self.game_over = False
        self.window = None

    def start(self):
        self.window = Window((400, 300))

        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.window.close()
