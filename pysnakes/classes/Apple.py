from random import randrange

class Apple:
    def __init__(self, dis_width, dis_height, snake_block, color):
        self.pos_x = round(randrange(0, (dis_width - snake_block) / 10) * 10)
        self.pos_y = round(randrange(0, (dis_height - snake_block) / 10) * 10)
        self.block = snake_block
        self.color = color