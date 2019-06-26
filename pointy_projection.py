import tkinter
import numpy as np
from PointyProjection import PointyProjection as Projection
from OrtogonalProjection import Base
from index import draw_cube, cube

u1 = np.array([1, 0, 0])
u2 = np.array([0, 1, 0])
u3 = np.array([0, 0, 1])
base = Base(u1, u2, u3)
p = Projection(50, np.array([200.0, -60.0, -400.0]), base)


def key_up(event):
    p.near -= 1


def key_down(event):
    p.near += 1


mouse_previous_point = None


def motion(event):
    global mouse_previous_point
    if mouse_previous_point is not None:
        move = event.x - mouse_previous_point[0], event.y - mouse_previous_point[1]
        print(move)
        base.rotate_x(move[1] * 0.001)
        base.rotate_y(move[0] * 0.001)
    mouse_previous_point = event.x, event.y


def key(event):
    if event.char == 'd':
        p.pv += base.base[:, 0] * 10
    elif event.char == 'a':
        p.pv -= base.base[:, 0] * 10
    elif event.char == 'w':
        p.pv += base.base[:, 2] * 20
    elif event.char == 's':
        p.pv -= base.base[:, 2] * 20


top = tkinter.Tk()
C = tkinter.Canvas(top, bg="white", height=1080, width=1920)
top.bind("<Up>", key_up)
top.bind("<Down>", key_down)
top.bind("<Key>", key)
top.bind("<Motion>", motion)


def main_loop():
    C.delete("all")
    C.pack()
    draw_cube(cube, p, C)
    top.after(17, main_loop)


top.after(0, main_loop)
top.mainloop()
