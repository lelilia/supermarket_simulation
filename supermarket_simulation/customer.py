from random import sample, randint
from supermarket_simulation.utils.constants import TILE_SIZE, STATE_LOCATION, OFS, SHOPPING_LIST
from supermarket_simulation.utils.a_star import find_path


class Customer:

    def __init__(self, customer_id, shopping_list = SHOPPING_LIST, speed = 4):
        self.id = customer_id
        self.state = 'entry'
        self.shopping_list = shopping_list
        self.x = STATE_LOCATION[self.state][0][0] * TILE_SIZE
        self.y = STATE_LOCATION[self.state][0][1] * TILE_SIZE
        self.speed = speed
        self.chosen_checkout = None
        self.items = 0
        self.path = []
        self.wait = 0

        # visualization
        self.image = sample([(0, 255, 0), (255, 0, 0), (0, 0, 255)], 1)
        self.size = 10

    def __repr__(self):
        return f'<Customer {self.id}: {self.state} {len(self.shopping_list)}, [{self.x}, {self.y }], path: {self.path}>'

    def send_to_position(self, x, y):
        this_location = (self.x // TILE_SIZE, self.y // TILE_SIZE)
        next_location = (x, y)

        if this_location != next_location:
            self.path = find_path(this_location, next_location)

    def back_to_aisle(self):
        self.state = 'back_to_aisle'
        x_pos = self.x // TILE_SIZE
        y_pos = self.y // TILE_SIZE
        if y_pos % 2 == 0:
            y_pos += 1
        self.path = [(x_pos, y_pos)]

    def pick_up_item(self):
        self.state = 'pick_up_item'
        x_pos = self.x // TILE_SIZE
        y_pos = self.y // TILE_SIZE
        if y_pos % 2 == 0:
            y_pos += 12.0 / TILE_SIZE
        else:
            y_pos -= 12.0 / TILE_SIZE
        self.path = [(x_pos, y_pos)]

    def get_path_to_next_location(self, next_position):
        if self.chosen_checkout is None:
            next_location = sample(STATE_LOCATION[next_position], 1)[0]
        else:
            next_location = self.chosen_checkout.end_of_queue

        this_location = (self.x // TILE_SIZE, self.y // TILE_SIZE)
        if this_location != next_location:
            self.path = find_path(this_location, next_location)

    def walk_to_next_item(self):
        self.state = 'walk_to_next_item'
        next_aisle = self.shopping_list[0]
        self.get_path_to_next_location(next_aisle)
        # next_location = sample(STATE_LOCATION[next_aisle], 1)[0]
        # this_location = (self.x // TILE_SIZE, self.y // TILE_SIZE)
        # if this_location != next_location:
        #     self.path = find_path(this_location, next_location)

    def next_state(self):
        if self.state == 'entry':
            self.walk_to_next_item()
            self.state = 'walking'
        elif self.state == 'checkout':
            if self.chosen_checkout:
                print('CHOOSEN')
                if self.chosen_checkout.current_customer != self and self not in self.chosen_checkout.queue:
                    self.get_path_to_next_location('checkout')
        elif self.state == 'pick_up_item':
            self.wait = 3 * self.speed
            self.shopping_list.pop(0)
            self.back_to_aisle()
        elif len(self.shopping_list) == 0:
            self.state = 'checkout'
        elif self.state == 'back_to_aisle':
            if len(self.shopping_list) == 0:
                print('ERRRRRRRORRRR')
            self.walk_to_next_item()
        else:
            self.pick_up_item()


    def walk(self):
        target = self.path[0]
        print(target)
        target_x, target_y = target[0] * TILE_SIZE, target[1] * TILE_SIZE

        if self.x == target_x and self.y  == target_y:
            self.path.pop(0)

            if len(self.path) > 0:
                target = self.path[0]
                target_x, target_y = target[0] * TILE_SIZE, target[1] * TILE_SIZE
            else:
                self.next_state()

        if self.x > target_x:
            self.x -= min(self.speed, self.x - target_x)
        elif self.x < target_x:
            self.x += min(self.speed, target_x - self.x)
        if self.y > target_y:
            self.y -= min(self.speed, self.y - target_y)
        elif self.y < target_y:
            self.y += min(self.speed, target_y - self.y)



    def move(self):
        print(self.id)
    #     if self.chosen_checkout:

    #         self.get_path_to_next_location('checkout')
        if self.wait > 0:
            self.wait -= 1

        elif len(self.path) > 0:
            print('walk')
            self.walk()
        else:
            print('next_stete', self.id)
            self.next_state()

    def draw(self, frame):
        x_pos = OFS + self.x + (TILE_SIZE // self.size) // 2
        y_pos = OFS + self.y + (TILE_SIZE // self.size) // 2
        frame[x_pos : x_pos + self.size, y_pos : y_pos + self.size] = self.image


if __name__ == '__main__':
    from supermarket_simulation.checkout import Checkout

    c = Customer(1)
    while c.state != 'checkout':
        print(c)
        c.move()

    c1 = Customer(2)
    c1.state = 'checkout'
    c2 = Customer(3)
    c1.state = 'checkout'
    checkout = Checkout(0, 9, 3)
    c.chosen_checkout = checkout
    c1.chosen_checkout = checkout
    c2.chosen_checkout = checkout

    while c.state != 'exit':
        print(c)
        print(checkout)
        c.move()
        c1.move()
        c2.move()
        checkout.move()