import time
from random import random

import numpy as np
import cv2

from supermarket_simulation.supermarket_map import SupermarketMap
from supermarket_simulation.supermarket import Supermarket
from supermarket_simulation.utils.constants import IMAGES, MARKET, TILES

class Simulation():
	def __init__(self):
		...

if __name__ == '__main__':
	background = np.zeros((700, 1000, 3), np.uint8)
	market = SupermarketMap(MARKET, TILES)
	supermarket = Supermarket(1)
	supermarket.add_new_customer()
	supermarket.add_cashier()
	supermarket.adding_prob = 0.01

	frame = background.copy()

	while len(supermarket.customers) > 0:
		market.draw(frame)
		supermarket.next_minute()
		supermarket.draw(frame)
		print(supermarket)
		supermarket.print_supermarket()

		cv2.imshow("frame", frame)
		time.sleep(0.1)
		key = chr(cv2.waitKey(1) & 0xFF)
		if key == 'q':
			break
	cv2.destroyAllWindows()
