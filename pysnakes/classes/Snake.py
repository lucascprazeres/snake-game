class Snake:
    def __init__(self, color, position):
        self.color = color
        self.size = (10, 10)
        (self.pos_x, self.pos_y) = position
        self.x_direction = 0
        self.y_direction = 0

    def change_direction(self, x, y):
        self.x_direction = x
        self.y_direction = y

    def move(self):
        self.pos_x += self.x_direction
        self.pos_y += self.y_direction