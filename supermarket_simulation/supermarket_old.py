
from random import random, randint
from supermarket_simulation.customer_old import Customer
from supermarket_simulation.cashier import Cashier
from supermarket_simulation.checkout_old import Checkout
from supermarket_simulation.utils.constants import STATE_LOCATION, WALKABLE_LIST
from supermarket_simulation.utils.a_star import find_path

class Supermarket():
	'''
	manages multiple Customer instances that are currently in the market.
	'''

	def __init__(self, adding_prob=0.01):
		self.customers = []
		self.cashiers = []
		self.checkouts = []
		self.time = 0
		self.last_customer_id = 0
		self.adding_prob = adding_prob
		self.end_of_entry_queue = 0


	def __repr__(self):
		return f'<Market {self.time}: {len(self.customers)} customers in the store >'

	def print_supermarket(self):
		for customer in self.customers:
			print(customer)

	def get_time(self):
		'''
		print current time in HH:MM format
		'''
		time_in_minutes = 7 * 60 + self.time // 30
		hours = time_in_minutes // 60
		minutes = time_in_minutes % 60
		return f'{str(hours).zfill(2)}:{str(minutes).zfill(2)}'

	@property
	def len_entry_queue(self):
		count = 0
		for customer in self.customers:
			if customer.x >= 11:
				count += 1
		return count

	def add_new_customer(self):
		if random() < self.adding_prob and len(self.customers) < 10 and self.len_entry_queue == 0:
			c = Customer(self.last_customer_id)
			self.last_customer_id += 1
			self.customers.append(c)

	def open_checkout(self):
		if len(self.cashiers) < 3:
			id = 2 - len(self.checkouts) 
			x = STATE_LOCATION['checkout'][id][0]
			y = STATE_LOCATION['checkout'][id][1]
			cashier = Cashier(x + 1, y + 1, randint(1,3))
			self.cashiers.append(cashier)
			checkout = Checkout(id, cashier, x, y)
			self.checkouts.append(checkout)

	def get_ends_of_checkout_queue(self):
		end_positions = []
		for checkout in self.checkouts:
			end_positions.append(checkout.end_of_queue)
		return end_positions

	def send_customer_to_checkout(self, customer):
		possible_checkouts = self.get_ends_of_checkout_queue()
		checkout_id = randint(0, len(self.checkouts) - 1)
		closest_checkout = possible_checkouts[checkout_id]
		customer.chosen_checkout = self.checkouts[checkout_id]
		#TODO find the true closest checkout
		customer.send_to_checkout(*closest_checkout)


	def remove_customers(self):
		for customer in self.customers:
			if not customer.is_active:
				self.customers.remove(customer)

	def can_customer_move(self, customer):
		for other_customer in self.customers:
			if customer.id == other_customer.id:
				continue
			if customer.path:
				if customer.path[0] == (other_customer.x, other_customer.y):
					print(other_customer.id, 'ist mir im weg', other_customer.x, other_customer.y)
					return False
		return True

	def next_minute(self):
		self.add_new_customer()
		self.time += 1
		for customer in self.customers:
			print(customer.id, 'can move', self.can_customer_move(customer))
			if customer.state == 'checkout':
				if not customer.is_checking_out and customer.items > 0:
					self.send_customer_to_checkout(customer)
					customer.is_checking_out = True
				# elif customer.chosen_checkout is not None:
				# 	checkout = customer.chosen_checkout
				# 	if len(customer.path) == 0 and customer not in checkout.queue and customer != checkout.current_customer:
				# 		checkout.add_customer(customer)
			if self.can_customer_move(customer):
				customer.move()
			# else:
			# 	# look for a new path
			# 	occupied_space = customer.path[0]
			# 	target_location = customer.path[-1]
			# 	if occupied_space != target_location:
			# 		# find new path else wait
			# 		walkable_list = WALKABLE_LIST.copy()
			# 		walkable_list.remove(occupied_space)

			# 		new_path= find_path((customer.x, customer.y), target_location, walkable_list=walkable_list)
			# 		if new_path:
			# 			customer.path = new_path

		self.remove_customers()
		for checkout in self.checkouts:
			checkout.checkout_customer()

	def draw(self, frame):
		for customer in self.customers:
			customer.draw(frame)
		for cashier in self.cashiers:
			cashier.draw(frame)

if __name__ == '__main__':
	from supermarket_simulation.customer import Customer
	c = Customer(0)
	c.x = 2
	c.y = 2
	c.state = 'fruit'
	c.shopping_list = ['fruit']
	m = Supermarket()
	m.customers.append(c)
	m.adding_prob = 0
	m.open_checkout()
	m.open_checkout()
	while len(m.customers) > 0:
		m.next_minute()
		print(m.get_ends_of_checkout_queue())
		print(m)
		m.print_supermarket()