import pygame

class Window:
    def __init__(self, canvas):
        self.canvas = dict(x=canvas[0], y=canvas[1])
        self.window = pygame.display.set_mode((self.canvas["x"], self.canvas["y"]))
        self.caption = pygame.display.set_caption("pySnakes by Lucas dos Prazeres")
        pygame.display.update()

    def close(self):
        pygame.quit()
        quit()