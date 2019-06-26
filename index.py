import tkinter
import numpy as np

cube = [np.array([0, 0, 0]),
        np.array([0, 0, 1]),
        np.array([0, 1, 0]),
        np.array([0, 1, 1]),
        np.array([1, 0, 0]),
        np.array([1, 0, 1]),
        np.array([1, 1, 0]),
        np.array([1, 1, 1])]

clear_cube = [200 * (v + np.array([1, 1, 1])) for v in cube]
cube = [200 * (v + np.array([-0.5, -0.5, -0.5])) for v in cube]


def draw_segment_projected(A, B, projection, canvas):
    offset = [300, 300]
    a = projection.localise(A)
    b = projection.localise(B)
    canvas.create_line(a[0] + offset[0], a[1] + offset[1], b[0] + offset[0], b[1] + offset[1])


def draw_cube(cube, projection, canvas):
    draw_segment_projected(cube[0], cube[1], projection, canvas)
    draw_segment_projected(cube[0], cube[2], projection, canvas)
    draw_segment_projected(cube[0], cube[4], projection, canvas)
    draw_segment_projected(cube[1], cube[3], projection, canvas)
    draw_segment_projected(cube[1], cube[5], projection, canvas)
    draw_segment_projected(cube[2], cube[3], projection, canvas)
    draw_segment_projected(cube[2], cube[6], projection, canvas)
    draw_segment_projected(cube[3], cube[7], projection, canvas)
    draw_segment_projected(cube[4], cube[5], projection, canvas)
    draw_segment_projected(cube[4], cube[6], projection, canvas)
    draw_segment_projected(cube[5], cube[7], projection, canvas)
    draw_segment_projected(cube[6], cube[7], projection, canvas)
