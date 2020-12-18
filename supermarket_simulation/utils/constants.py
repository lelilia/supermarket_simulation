import cv2
from random import randint

from supermarket_simulation.utils.functions import build_grid, walkable, TILES, build_large_grid

ITEMS = [
	'toiletpaper',
	'bananas',
	'water',
]


TILE_SIZE = 32
OFS = 50

IMAGES = {
    'wall': TILES[:TILE_SIZE, :TILE_SIZE]
}

MARKET = """
##################
##..............##
##..##..##..##..##
##..##..##..##..##
##..##..##..##..##
##..##..##..##..##
##..##..##..##..##
##...............#
##..C#..C#..C#...#
##..##..##..##...#
##...............#
##############GG##
""".strip()

ALL_STATES = ['checkout', 'dairy', 'drinks',
              'fruit', 'spices', 'entry', 'exit']

STATE_LOCATION = {
    'dairy':    [(2, 2), (2, 3), (3, 2), (3, 3), (4, 2), (4, 3), (5, 2), (5, 3), (6, 2), (6, 3)],
    'drinks':   [(2, 6), (2, 7), (3, 6), (3, 7), (4, 6), (4, 7), (5, 6), (5, 7), (6, 6), (6, 7)],
    'fruit':    [(2, 10), (2, 11), (3, 10), (3, 11), (4, 10), (4, 11), (5, 10), (5, 11), (6, 10), (6, 11)],
    'spices':   [(2, 14), (2, 15), (3, 14), (3, 15), (4, 14), (4, 15), (5, 14), (5, 15), (6, 14), (6, 15)],
    'checkout': [(8, 3), (8, 7), (8, 11)],
    'entry':    [(11, 15)],
    'exit':     [(11, 14)]
}

POSSIBLE_MOVES_DIAGONAL = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1)]

POSSIBLE_MOVES = [(-1, 0), (0, -1), (0, 1), (1, 0)]

GRID = build_grid(MARKET)

WALKABLE_LIST = walkable(GRID)

LARGE_GRID = build_large_grid(MARKET, TILE_SIZE)
LARGE_WALKABLE_LIST = walkable(LARGE_GRID)

SHOPPING_LIST = ['spices'] * randint(1,2) + ['fruit'] * randint(0,2) + ['drinks'] * randint(0, 2) + ['dairy'] * randint(0,2)