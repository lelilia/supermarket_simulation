import numpy as np
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

from supermarket_simulation.utils.constants import MARKET

matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

grid = Grid(matrix=matrix)

start = grid.node(0,0)
end = grid.node(2,2)

finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
path, runs = finder.find_path(start, end, grid)

print('operations:', runs, 'path length:', len(path))
print(grid.grid_str(path=path, start=start, end=end))

print(path)

def build_grid(market):
    grid = []
    for m in market.split('\n'):
        grid.append([1 if t in '.G' else 0 for t in m])
    return np.array(grid)

matrix = build_grid(MARKET)
print(matrix)

grid = Grid(matrix=matrix)
start = grid.node(14,11)
end = grid.node(10,2)

finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
path,run = finder.find_path(start, end, grid)
print(run)
print(path)
print(grid.grid_str(path=path, start=start, end=end))