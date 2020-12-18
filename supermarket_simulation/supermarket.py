
from random import random
from supermarket_simulation.customer import Customer
from supermarket_simulation.cashier import Cashier

class Supermarket():
	'''
	manages multiple Customer instances that are currently in the market.
	'''

	def __init__(self, adding_prob=0.02):
		self.customers = []
		self.cashiers = []
		self.time = 0
		self.last_customer_id = 0
		self.adding_prob = adding_prob


	def __repr__(self):
		return f'<Market {self.time}: {len(self.customers)} customers in the store >'

	def print_supermarket(self):
		for customer in self.customers:
			print(customer)

	def get_time(self):
		time = self.time // 30
		hour = time // 60 + 7
		minute = time % 60
		return f'{str(hour).zfill(2)}:{str(minute).zfill(2)}'

	def add_new_customer(self):
		if random() < self.adding_prob:
			c = Customer(self.last_customer_id)
			self.last_customer_id += 1
			self.customers.append(c)

	def add_cashier(self):
		if len(self.cashiers) < 3:
			x = 9
			y = 5
			speed = 3
			cashier = Cashier(x, y, speed)
			self.cashiers.append(cashier)


	def remove_customers(self):
		for customer in self.customers:
			if not customer.is_active:
				self.customers.remove(customer)

	def next_minute(self):
		self.add_new_customer()
		self.time += 1
		for customer in self.customers:
			customer.move()
		self.remove_customers()

	def draw(self, frame):
		for customer in self.customers:
			customer.draw(frame)
		for cashier in self.cashiers:
			cashier.draw(frame)

if __name__ == '__main__':
	m = Supermarket()
	for i in range(10):
		m.next_minute()
		print(m)
		m.print_supermarket()