import pygame

COLORS = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "black": (0, 0, 0),
    "white": (255, 255, 255)
}

class Window:
    def __init__(self, canvas):
        self.canvas = dict(x=canvas[0], y=canvas[1])
        self.surface = pygame.display.set_mode((self.canvas["x"], self.canvas["y"]))
        self.caption = pygame.display.set_caption("pySnakes by Lucas dos Prazeres")

    def close(self):
        pygame.quit()
        quit()