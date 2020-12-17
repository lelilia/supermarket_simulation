import numpy as np
import cv2

img = cv2.imread('graphics/market.png')

class Customer:
    def __init__(self, x, y, v_x, v_y):
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.color = (255,0,0)
        self.image = cv2.imread('graphics/Phantom_Open_Emoji_1f603.png')
        self.radius = 10

    def move(self):
        if not (self.radius <= self.x + self.v_x <= HEIGHT - self.radius):
        #if not (0 <= self.x + self.v_x <= HEIGHT - self.size):
            self.v_x *= -1
        self.x += self.v_x
        if not (self.radius <= self.y + self.v_y <= WIDTH - self.radius):
        # if not (0 <= self.y + self.v_y <= WIDTH- self.size):
            self.v_y *= -1

        self.y += self.v_y

    def draw(self, frame):
        frame[self.x - self.radius : self.x + self.radius, self.y - self.radius : self.y + self.radius] = self.color

class Wall:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.height = height
        self.width = width


    def draw(self, frame):
        frame[self.x : self.x + self.height, self.y : self.y + self.width] = (255, 0, 0)

class Supermarket:
    def __init__(self):
        self.customers = []
        self.aisles = []

    def add_aisle(self, x, y, width, height):
        a = Wall(x, y, width, height)
        self.aisles.append(a)

    def add_customer(self):

        c = Customer(600, 837, -1, 0 )
        self.customers.append(c)

    # def is_touching_wall(self, customer, aisle):
    #     if customer.x + customer.radius <= aisle.x or customer.x - customer.radius >= aisle.x + aisle.height:
    #         customer.v_x *= 1
    #     if customer.y + customer.radius <= aisle.y or customer.y - customer.radius >= aisle.y + aisle.width:
    #         customer.v_y *= 1

    #     return not (customer.x + customer.radius <= aisle.x or \
    #                 customer.x - customer.radius >= aisle.x + aisle.height or \
    #                 customer.y + customer.radius <= aisle.y or \
    #                 customer.y - customer.radius >= aisle.y + aisle.width)

    # def check_for_wall_collisions(self):
    #     for c in self.customers:
    #         for a in self.aisles:
                # if self.is_touching_wall(c, a):
                #     print('touching')
                #     c.v_y *= -1
                #     c.v_x *= -1

    def move(self):
        # self.check_for_wall_collisions()
        for c in self.customers:

            c.move()

    def draw(self, frame):
        for c in self.customers:
            c.draw(frame)
        for a in self.aisles:
            a.draw(frame)


    

WIDTH = 943
HEIGHT = 675


running = True
time = 0

s = Supermarket()
s.add_customer()


while running:
    time += 1
    frame = img.copy()
    s.move()
    s.draw(frame)
    cv2.imshow("frame", frame)
    key = chr(cv2.waitKey(1) & 0xFF)
    if key == 'q':
        break

cv2.destroyAllWindows()
