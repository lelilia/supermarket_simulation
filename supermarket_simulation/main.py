import time
from random import random

import numpy as np
import cv2

from supermarket_simulation.supermarket_map import SupermarketMap
from supermarket_simulation.supermarket import Supermarket
from supermarket_simulation.utils.constants import IMAGES, MARKET, TILES

class Simulation():
	def __init__(self):
		self.frame = np.zeros((700, 1000, 3), np.uint8)
		self.market = SupermarketMap(MARKET, TILES)
		self.supermarket = Supermarket()
		self.go = True

	def run(self):
		self.supermarket.add_cashier()
		
		while self.go:
			self.market.draw(self.frame)
			self.supermarket.next_minute()
			self.supermarket.draw(self.frame)
			print(self.supermarket)
			self.supermarket.print_supermarket()

			cv2.imshow("frame", self.frame)
			time.sleep(0.1)
			key = chr(cv2.waitKey(1) & 0xFF)
			if key == 'q':
				self.go = False
			if self.supermarket.minutes > 7 * 60 * 30 + 1000:
				self.go = False
		cv2.destroyAllWindows()

if __name__ == '__main__':
	simulation = Simulation()
	simulation.run()

	# background = np.zeros((700, 1000, 3), np.uint8)
	# market = SupermarketMap(MARKET, TILES)
	# supermarket = Supermarket(1)
	# supermarket.add_new_customer()
	# supermarket.add_cashier()
	# supermarket.adding_prob = 0.01

	# frame = background.copy()

	# while len(supermarket.customers) > 0:
	# 	market.draw(frame)
	# 	supermarket.next_minute()
	# 	supermarket.draw(frame)
	# 	print(supermarket)
	# 	supermarket.print_supermarket()

	# 	cv2.imshow("frame", frame)
	# 	time.sleep(0.1)
	# 	key = chr(cv2.waitKey(1) & 0xFF)
	# 	if key == 'q':
	# 		break
	# cv2.destroyAllWindows()
