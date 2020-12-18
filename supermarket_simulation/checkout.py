from supermarket_simulation.utils.constants import OFS, TILE_SIZE
from supermarket_simulation.customer import Customer

class Checkout:
    def __init__(self, id, x, y, speed=5):
        self.id = id
        self.x = x + 1
        self.y = y + 2
        self.speed = speed
        self.queue = []
        self.current_customer = None
        self.end_of_queue = [x, y]
        self.time = 0
        # visualization
        self.image = (0, 255, 0)
        self.size = 10

    def __repr__(self):
        return f'<{self.current_customer}\n-------------------{self.queue}>'

    def add_customer(self, customer):
        if len(self.queue) == 0 and self.current_customer is None:
            self.current_customer = customer
        else:
            self.queue.append(customer)
            self.end_of_queue[0] -= 1

    def move(self):
        if self.current_customer:
            if self.current_customer.items > 0:
                if self.time < self.speed:
                    self.time += 1
                else:
                    self.current_customer.items -= 1
                    self.time = 0
            else:
                self.current_customer.state = 'exit'
                self.current_customer = None
        else:
            if self.queue:
                self.current_customer = self.queue.pop(0)
                for customer in self.queue:
                    x_pos = customer.x // TILE_SIZE + 1
                    y_pos = customer.y
                    customer.send_to_position(x_pos, y_pos)
                self.end_of_queue[0] += 1

    def draw(self, frame):
        x_pos = OFS + self.x * TILE_SIZE + (TILE_SIZE - self.size) // 2
        y_pos = OFS + self.y * TILE_SIZE + (TILE_SIZE - self.size) // 2

        frame[x_pos : x_pos + self.size, y_pos : y_pos + self.size] = self.image

if __name__ == '__main__':
    checkout = Checkout(1, 3, 4)
    c1 = Customer(1)
    c1.items = 3
    checkout.add_customer(c1)
    print(checkout)
    checkout.move()
    print(checkout)
    c = Customer(2)
    c.items = 3
    checkout.add_customer(c)
    c = Customer(3)
    c.items = 1
    checkout.add_customer(c)
    while checkout.queue:
        print(checkout)
        checkout.move()