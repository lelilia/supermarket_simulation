''' A* Algorithm to find the shortest path'''

import operator
import numpy as np

from supermarket_simulation.utils.constants import MARKET, POSSIBLE_MOVES, GRID, WALKABLE_LIST


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


# GRID = build_grid(MARKET)
# WALKABLE_LIST = walkable(GRID)

def heuristic(current: list, target: list) -> int:
    """
    Calculate the estimated Distance between current node and target node based on Manhattan Distance
    """
    return (abs(target[0] - current[0]) + abs(target[1] - current[1]))


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

def get_turning_points_from_path(path):
    dx_old = dy_old = 0
    last_pos = path[0]
    turning_points = []
    for step in path[1:]:
        dx = step[0] - last_pos[0]
        dy = step[1] - last_pos[1]
        if not(dx == dx_old and dy == dy_old):
            turning_points.append(last_pos)
        dx_old, dy_old, last_pos = dx, dy, step
    turning_points.append(path[-1])
    return turning_points


def get_path_from_target(current):
    backwards = []
    while current:
        backwards.append(current.location)
        current = current.parent
    return backwards[::-1]


def create_neighbours(poss_moves, current_node, target_node, grid_array, frontier, walkable_list):
    for move in poss_moves:
        node_position = (current_node.location[0] + move[0], current_node.location[1] + move[1])
        if node_position in walkable_list:
            neighbour = Node(parent=current_node,
                             location = node_position,
                             cost = current_node.cost + 1,
                             heur = heuristic(node_position, target_node.location))
            frontier.append(neighbour)
    return frontier


def find_path(start, target, grid_array=GRID, p_moves=POSSIBLE_MOVES, walkable_list=WALKABLE_LIST):
    start_node = Node(None, start)
    target_node = Node(None, target)
    frontier = [start_node]

    while frontier:
        frontier.sort(key=operator.attrgetter('f_value'))
        #current_node = frontier.pop(0)
        current_node = frontier[0]
        frontier.pop(0)

        if current_node.location == target_node.location:
            shortest_path = get_path_from_target(current_node)
            return shortest_path

        frontier = create_neighbours(p_moves, current_node, target_node, grid_array, frontier, walkable_list)


class Node():
    def __init__(self, parent, location, cost=0, heur=0):
        self.parent = parent
        self.location = location
        self.cost = cost
        self.heur = heur
        self.f_value = self.cost + self.heur



#
# grid = build_grid()
# print(grid)

if __name__ == '__main__':
    start_given = (9,3)
    target_given = (11,14)
    path = find_path(start_given, target_given)
    print(path)


