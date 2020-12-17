import cv2
import numpy as np

TILES = cv2.imread("./graphics/tiles.png")

def build_grid(market):
    grid = []
    for m in market.split('\n'):
        grid.append([0 if t in '.G' else 1 for t in m])
    return np.array(grid)

def walkable(grid_array: list) -> list:
    """Get a list of all the coordinates that are walkable

    Args:
        grid_array (list): map of the terrain

    Returns:
        list: all coordinates that are walkable
    """
    walkable = []
    for i, row in enumerate(grid_array):
        for j, cell in enumerate(row):
            if cell == 0:
                walkable.append((i, j))
    return walkable