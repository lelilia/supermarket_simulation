from random import random, randint

from supermarket_simulation.customer import Customer
from supermarket_simulation.utils.constants import STATE_LOCATION

class Supermarket:
    def __init__(self, propability_for_new_customer = 0.05):
        self.customers = []
        self.checkouts = []
        self.time = 7 * 60 * 30
        self.last_customer_id = 0
        self.propability_for_new_customer = propability_for_new_customer

    def __repr__(self):
        return f'<Supermarket {self.time}: {len(self.customers)} customers in the store.>'

    def print_customers(self):
        for customer in self.customers:
            print(customer)

    def get_time(self):
        hour = self.time // 1800
        minutes = self.time // 30 % 60
        return f'{str(hour).zfill(2)}:{str(minutes).zfill(2)}'

    def add_new_customer(self):
        if random() < self.propability_for_new_customer:
            speed = 2 ** randint(1,2)
            c = Customer(self.last_customer_id, speed=speed)
            self.last_customer_id += 1
            self.customers.append(c)

    def remove_customers(self, customer):
        self.customers.remove(customer)

    def open_checkout(self):
        if len(self.checkouts) < 3:
            id = 3 - len(self.checkouts) - 1
            print(id)
            x, y = STATE_LOCATION['checkout'][id]

    def assign_customer_to_checkout(self, customer):
        if len(self.checkouts) == 1:
            customer.chosen_checkout = self.checkouts[0]
        # TODO: add more checkouts

    def move(self):
        self.add_new_customer()
        for customer in self.customers:
            if customer.state == 'checkout' and customer.chosen_checkout is None:
                self.assign_customer_to_checkout(customer)
            elif customer.state == 'exit' and len(customer.path) == 0:
                self.remove_customers(customer)
            customer.move()
        for checkout in self.checkouts:
            checkout.move()
        self.time += 1

    def draw(self, frame):
        for customer in self.customers:
            customer.draw(frame)
        for checkout in self.checkouts:
            checkout.draw(frame)

