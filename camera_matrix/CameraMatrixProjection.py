import numpy as np
import tkinter
import index


class CameraProjection:

    def __init__(self, f):
        self.f = f
        self.camera_matrix = None
        self.x_angle = 0
        self.y_angle = 0
        self.z_angle = 0
        self.transposition = np.array([0, 0, 0])
        self.rotation = np.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.setF(f)
        self.camera_pos = np.array([0, 0, 0])

    def setF(self, f):
        self.f = f
        self.camera_matrix = np.column_stack(
            [np.array([f, 0, 0]), np.array([0, f, 0]), np.array([0, 0, 1]), np.array([0, 0, 0])])

    def rotation_matrix(self):
        x = self.x_angle
        y = self.y_angle
        z = self.z_angle
        x_rotation = np.matrix([[1, 0, 0], [0, np.cos(x), -np.sin(x)], [0, np.sin(x), np.cos(x)]])
        y_rotation = np.matrix([[np.cos(y), 0, np.sin(y)], [0, 1, 0], [-np.sin(y), 0, np.cos(y)]])
        z_rotation = np.matrix([[np.cos(z), -np.sin(z), 0], [np.sin(z), np.cos(z), 0], [0, 0, 1]])
        rotation = x_rotation.dot(y_rotation.dot(z_rotation))
        return rotation

    def m_matrix(self):
        t = self.transposition
        rotation = self.rotation_matrix()

        output = np.block([
            [rotation, t.reshape((3, 1))],
            [0, 0, 0, 1]
        ])

        self.rotation = rotation
        self.camera_pos = np.squeeze(np.asarray(-np.linalg.inv(rotation).dot(np.squeeze(np.asarray(t)))))

        return output

    def localise(self, x):
        x = np.append(x, [1])
        m = self.m_matrix()
        c = np.append(self.transposition, [1])
        # l = self.get_lookup_vector()
        # l = np.squeeze(np.asarray(l))
        # c = np.append(l, [1])
        h = m.dot(x - c)
        h = np.squeeze(np.asarray(h))
        y = self.camera_matrix.dot(h)
        y = y / y[2]
        return y

    def get_lookup_vector(self):
        u, w, v = self.rotation[:, 0], self.rotation[:, 1], self.rotation[:, 2]
        n = u + w + v
        norm = np.linalg.norm(n)
        return n / norm
