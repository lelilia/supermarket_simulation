""" customer class """
from random import sample, randint
from supermarket_simulation.utils.constants import TILE_SIZE, STATE_LOCATION, OFS
from supermarket_simulation.utils.functions import TILES
from supermarket_simulation.utils.a_star import find_path

class Customer:

    def __init__(self, customer_id):
        self.id = customer_id
        self.state = 'entry'
        self.shopping_list = ['spices'] + ['fruit'] * randint(0,2) + ['drinks'] * randint(0, 2) + ['dairy'] * randint(0,2)
        self.x = STATE_LOCATION[self.state][0][0]
        self.y = STATE_LOCATION[self.state][0][1]
        self.v = 4
        self.path = []
        self.dx = 0
        self.dy = 0
        self.picked_up_item = True
        self.pick_up_time = 0
        self.items = 0
        self.is_checking_out = False
        self.chosen_checkout = None

        #TODO speed for pick up and speed for walking
        # visualization
        # self.image = TILES[8 * TILE_SIZE: 9 * TILE_SIZE,
        #                    3 * TILE_SIZE: (3 + 1) * TILE_SIZE]
        self.image = (255, 0, 0)
        self.size = 10

    def __repr__(self):
        return f'<Customer {self.id}: {self.state}, ({self.x} + {self.dx}, {self.y} + {self.dy}) path: {self.path} moving {self.is_moving} checkingout {self.is_checking_out} {self.chosen_checkout is None}>'

    @property
    def is_active(self):
        if self.state == 'exit' and self.last_state == 'exit':
            return False
        return True


    @property
    def is_moving(self):
        if len(self.path) > 0:
            return True
        return False

    def send_to_checkout(self, x, y):
        next_location = (x, y)
        if (self.x, self.y) != next_location:
            self.path = find_path((self.x, self.y), next_location)

    def send_to_exit(self):
        self.state = 'exit'
        self.path = find_path((self.x, self.y), STATE_LOCATION[self.state][0])

    def next_state(self):
        if len(self.shopping_list) > 0:
            self.state, *self.shopping_list = self.shopping_list
            self.picked_up_item = False
        elif self.items > 0:
            self.state == 'checkout'
        else:
            self.state = 'exit'

        next_location = sample(STATE_LOCATION[self.state],1)[0]
        if self.state == 'checkout':
            next_location = (8, 11)
        this_location = (self.x, self.y)
        if this_location != next_location:
            self.path = find_path(this_location, next_location)


    def walk(self):

        target = self.path[0]
        if self.x == target[0] and self.y == target[1] :
            self.path.pop(0)
            if len(self.path)>0:
                target = self.path[0]

        if self.x > target[0] :
            self.dx -= self.v
        elif self.x < target[0] :
            self.dx += self.v
        if self.y > target[1] :
            self.dy -= self.v
        elif self.y < target[1] :
            self.dy += self.v

        if self.dx % TILE_SIZE == 0:
            self.x += self.dx // TILE_SIZE
            self.dx = 0
        if self.dy % TILE_SIZE == 0:
            self.y += self.dy // TILE_SIZE
            self.dy = 0

    def move_back_from_item(self):
        if self.y % 2 == 0:
            self.dy += 4
        else:
            self.dy -= 4

    def pick_up_item(self):
        if abs(self.dy) == 12:
            if self.pick_up_time < 3 * self.v:
                self.pick_up_time += 1
            else:
                self.picked_up_item = True
                self.pick_up_time = 0
                self.items += 1

        elif self.y % 2 == 0:
            self.dy -= 4
        else:
            self.dy += 4


    def move(self):
        if len(self.path) > 0:
            print(self.id, 'is walking')
            self.walk()
        elif not self.picked_up_item:
            self.pick_up_item()
        elif self.dy != 0:
            self.move_back_from_item()
        else:
            self.next_state()

    def draw(self, frame):
        x_pos = OFS + self.x * TILE_SIZE + self.dx + (TILE_SIZE - self.size) // 2
        y_pos = OFS + self.y * TILE_SIZE + self.dy + (TILE_SIZE - self.size) // 2
        # frame[y_pos: y_pos + TILE_SIZE, x_pos: x_pos + TILE_SIZE] = self.image
        frame[x_pos: x_pos + self.size, y_pos: y_pos + self.size] = self.image

if __name__ == '__main__':
    c = Customer(1)
    print(c)
    print(c.state)
    print(STATE_LOCATION['exit'])
    print(sample(STATE_LOCATION['entry'], 1))

    while c.is_active:
        print(c)
        print(c.picked_up_item)
        c.move()