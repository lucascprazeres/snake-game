class Snake:
    def __init__(self, color, position, block):
        self.color = color
        self.block = block
        self.head = []
        self.body = []
        self.length = 1
        (self.pos_x, self.pos_y) = position
        self.x_direction = 0
        self.y_direction = 0

    def change_direction(self, x, y):
        self.x_direction = x
        self.y_direction = y

    def move(self):
        self.pos_x += self.x_direction
        self.pos_y += self.y_direction

