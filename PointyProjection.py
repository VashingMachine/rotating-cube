import numpy as np


class PointyProjection:
    def __init__(self, near, pv, base):
        self.near = near
        self.pv = pv
        self.base = base

    def localise(self, p):
        p = self.base.localise(p)
        pv = self.base.localise(self.pv)
        x = pv[0] - p[0]
        y = pv[1] - p[1]
        h = pv[2] - p[2] - self.near
        f = h / (h + self.near)
        return np.array([x * f, y * f])
