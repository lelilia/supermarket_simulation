import time
from random import random

import numpy as np
import cv2

from supermarket_simulation.supermarket_map import SupermarketMap
from supermarket_simulation.supermarket import Supermarket
from supermarket_simulation.utils.constants import IMAGES, MARKET, TILES

class Simulation():
	def __init__(self):
		self.background = np.zeros((700, 1000, 3), np.uint8)
		self.market = SupermarketMap(MARKET, TILES)
		self.supermarket = Supermarket()
		self.go = True

	def run(self):
		self.supermarket.add_cashier()
		
		while self.go:
			frame = self.background.copy()
			self.market.draw(frame)
			self.supermarket.next_minute()
			self.supermarket.draw(frame)
			print(self.supermarket)
			self.supermarket.print_supermarket()
			cv2.putText(frame, self.supermarket.get_time(), (50, 35), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (255, 255, 255), 3)
			cv2.imshow("frame", frame)
			time.sleep(0.1)
			key = chr(cv2.waitKey(1) & 0xFF)
			if key == 'q':
				self.go = False
			if self.supermarket.time > 7 * 60 * 30 + 1000:
				self.go = False
		cv2.destroyAllWindows()

if __name__ == '__main__':
	simulation = Simulation()
	simulation.run()
