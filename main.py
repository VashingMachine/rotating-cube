import tkinter
import numpy as np
import scipy.linalg as la


class Base:
    def __init__(self, v, w):
        self.base = np.column_stack([v, w])
        self.normalize()
        pass

    def normalize(self):
        # self.base = la.orth(self.base)
        # Gram - Schmitd ortonormalization
        u1 = self.base[:, 0]
        u2 = self.base[:, 1]

        u2 = u2 - u2.dot(u1) / u1.dot(u1) * u1
        u1 = u1 / np.linalg.norm(u1)
        u2 = u2 / np.linalg.norm(u2)

        self.base = np.column_stack([u1, u2])
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



    def localise(self, v):
        return v.dot(self.base[:, 0]), v.dot(self.base[:, 1])

    def __str__(self):
        return self.base.__str__()


def draw_segment_projected(A, B, base, canvas):
    offset = [300, 300]
    a = base.localise(A)
    b = base.localise(B)
    canvas.create_line(a[0] + offset[0], a[1] + offset[1], b[0] + offset[0], b[1] + offset[1])


def draw_cube(cube, base, canvas):
    draw_segment_projected(cube[0], cube[1], base, canvas)
    draw_segment_projected(cube[0], cube[2], base, canvas)
    draw_segment_projected(cube[0], cube[4], base, canvas)
    draw_segment_projected(cube[1], cube[3], base, canvas)
    draw_segment_projected(cube[1], cube[5], base, canvas)
    draw_segment_projected(cube[2], cube[3], base, canvas)
    draw_segment_projected(cube[2], cube[6], base, canvas)
    draw_segment_projected(cube[3], cube[7], base, canvas)
    draw_segment_projected(cube[4], cube[5], base, canvas)
    draw_segment_projected(cube[4], cube[6], base, canvas)
    draw_segment_projected(cube[5], cube[7], base, canvas)
    draw_segment_projected(cube[6], cube[7], base, canvas)


u1 = np.array([0, 0, 1])
u2 = np.array([1, 0, 0])
base = Base(u1, u2)
cube = [np.array([0, 0, 0]),
        np.array([0, 0, 1]),
        np.array([0, 1, 0]),
        np.array([0, 1, 1]),
        np.array([1, 0, 0]),
        np.array([1, 0, 1]),
        np.array([1, 1, 0]),
        np.array([1, 1, 1])]

cube = [200 * (v + np.array([-0.5, -0.5, -0.5])) for v in cube]

base.rotate_z(0.2)

mouse_event_start = None

def button_start(event):
    global mouse_event_start
    mouse_event_start = event


def button_click(event):
    global mouse_event_start
    base.rotate_x(-(event.x - mouse_event_start.x) * 0.01)
    base.rotate_z((event.y - mouse_event_start.y) * 0.01)
    mouse_event_start = event


top = tkinter.Tk()
C = tkinter.Canvas(top, bg="white", height=600, width=800)
C.bind("<B1-Motion>", button_click)
C.bind("<Button-1>", button_start)


def main_loop():
    C.delete("all")
    draw_cube(cube, base, C)
    C.pack()
    top.after(17, main_loop)


top.after(0, main_loop)
top.mainloop()
