"""
Implement a customer that is moving around
between the sections of a supermarket
"""
import numpy as np
import cv2
import random

img = cv2.imread('images/market.png')

PURPLE = (255, 0, 255)    # (blue, green, red)
GREEN = (0, 128, 0)
BLUE = (255, 0, 0)
COLORS = [PURPLE, GREEN, BLUE]

AISLES = [100, 300, 550, 800]
CHECKOUTS = [100, 250, 400, 550]


class Customer:

    def __init__(self):
        self.size = 30
        self.color = random.choice(COLORS)
        self.location = [800, 800 +  + random.randint(1, 50)]
        self.speed = 1
        self.target_gen = self.get_next_target()
        self._target = next(self.target_gen)
        self._staying = random.randint(10, 2000) # cycles to wait

    def draw(self, frame):
        y = self.location[0]
        x = self.location[1]
        frame[y:y + self.size, x:x + self.size, :] = self.color

    def get_next_target(self):
        # go to starting point
        yield [460, 800]
        while True:
            # go to new aisle or checkout
            if random.randint(1, 6) < 6:
                yield [100 + random.randint(1, 300),\
                      random.choice(AISLES) + random.randint(1, 20)]
            else:
                yield [800, random.choice(CHECKOUTS)]
                while True:
                    yield [1000, 800]
            # leave
            self._staying = random.randint(10, 100)
            y = random.choice([60, 460])
            y += random.randint(1, 20)
            yield [y, self.location[1]]

    def move(self):
        if self._staying == 0:
            if self.location[1] > self._target[1]: # moves left
                self.location[1] -= self.speed
            elif self.location[1] < self._target[1]: # moves right
                self.location[1] += self.speed
            elif self.location[0] < self._target[0]: # moves down
                self.location[0] += self.speed
            elif self.location[0] > self._target[0]: # moves up
                self.location[0] -= self.speed
            else:
                self._target = next(self.target_gen)
        else:
            self._staying -= 1


# Main Program starts here
customers = [Customer() for i in range(50)]

while True:
    frame = img.copy()  # NumPy array (xsize, ysize, 3) dtype=uint8
    for c in customers:
        c.move()
        c.draw(frame)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cv2.destroyAllWindows()
