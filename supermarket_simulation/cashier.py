'''cashier class'''
from supermarket_simulation.utils.constants import OFS, TILE_SIZE

class Cashier():
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed_per_item = speed
        self.image = (0, 255, 0)
        self.size = 10

    def draw(self, frame):
        x_pos = OFS + self.x * TILE_SIZE  + (TILE_SIZE - self.size) // 2
        y_pos = OFS + self.y * TILE_SIZE  + (TILE_SIZE - self.size) // 2
        # frame[y_pos: y_pos + TILE_SIZE, x_pos: x_pos + TILE_SIZE] = self.image
        frame[x_pos: x_pos + self.size, y_pos: y_pos + self.size] = self.image
