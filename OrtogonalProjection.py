import numpy as np


class Base:
    def __init__(self, v, w, u):
        self.base = np.column_stack([v, w, u])
        self.normalize()
        pass


    def normalize(self):
        # self.base = la.orth(self.base)
        # Gram - Schmitd ortonormalization
        u1 = self.base[:, 0]
        u2 = self.base[:, 1]
        u3 = self.base[:, 2]

        u2 = u2 - u2.dot(u1) / u1.dot(u1) * u1
        u3 = u3 - u3.dot(u1) / u1.dot(u1) * u1 - u3.dot(u2) / u2.dot(u2) * u2
        u1 = u1 / np.linalg.norm(u1)
        u2 = u2 / np.linalg.norm(u2)
        u3 = u3 / np.linalg.norm(u3)

        self.base = np.column_stack([u1, u2, u3])
        pass

    def rotate_z(self, a):
        rotation_matrix = np.matrix([[np.cos(a), -np.sin(a), 0], [np.sin(a), np.cos(a), 0], [0, 0, 1]])
        self.base = rotation_matrix.dot(self.base)
        self.base = np.squeeze(np.asarray(self.base))
        pass

    def rotate_x(self, a):
        rotation_matrix = np.matrix([[1, 0, 0], [0, np.cos(a), -np.sin(a)], [0, np.sin(a), np.cos(a)]])
        self.base = rotation_matrix.dot(self.base)
        self.base = np.squeeze(np.asarray(self.base))

    def rotate_y(self, a):
        rotation_matrix = np.matrix([[np.cos(a), 0, np.sin(a)], [0, 1, 0], [-np.sin(a), 0, np.cos(a)]])
        self.base = rotation_matrix.dot(self.base)
        self.base = np.squeeze(np.asarray(self.base))

    def localise(self, v):
        # change later to matrix multiplication
        return v.dot(self.base[:, 0]), v.dot(self.base[:, 1]), v.dot(self.base[:, 2])

    def __str__(self):
        return self.base.__str__()
