import time
from random import random

import numpy as np
import cv2

from supermarket_simulation.supermarket_map import SupermarketMap
from supermarket_simulation.supermarket_old import Supermarket
from supermarket_simulation.customer_old import Customer
from supermarket_simulation.utils.constants import IMAGES, MARKET, TILES

class Simulation():
	def __init__(self):
		...

if __name__ == '__main__':
	background = np.zeros((700, 1000, 3), np.uint8)
	market = SupermarketMap(MARKET, TILES)
	supermarket = Supermarket(0.1)

	supermarket.open_checkout()

	frame = background.copy()

	co = supermarket.checkouts[0]

	while supermarket.time < 7 * 60 * 30 + 1000:

		frame = background.copy()
		market.draw(frame)
		supermarket.next_minute()
		supermarket.draw(frame)
		print(supermarket)
		supermarket.print_supermarket()
		print(co)

		cv2.putText(frame, supermarket.get_time(), (50,40), cv2.FORMATTER_FMT_DEFAULT, 1, (255, 255, 255),3)
		cv2.imshow("frame", frame)
		time.sleep(0.1)
		key = chr(cv2.waitKey(1) & 0xFF)
		if key == 'q':
			break
	cv2.destroyAllWindows()
