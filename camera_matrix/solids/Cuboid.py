import numpy as np

class Cuboid:
    def __init__(self, position, depth, height, width):
        self.position = position
        self.coords = [np.array([0, 0, 0]),
                       np.array([0, 0, depth]),
                       np.array([0, height, 0]),
                       np.array([0, height, depth]),
                       np.array([width, 0, 0]),
                       np.array([width, 0, depth]),
                       np.array([width, height, 0]),
                       np.array([width, height, depth])]
        self.coords = [v + position for v in self.coords]
        self.edges = [(0, 1), (0, 2), (0, 4), (1, 3), (1, 5), (2, 3), (2, 6), (3, 7), (4, 5), (4, 6), (5, 7), (6, 7)]
