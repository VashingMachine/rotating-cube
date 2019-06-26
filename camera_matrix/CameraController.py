import numpy as np


class Controller:
    def __init__(self, camera, drawer):
        self.camera = camera
        self.drawer = drawer

        self.drawer.register_binding("<Up>", self.key_up)
        self.drawer.register_binding("<Down>", self.key_down)
        self.drawer.register_binding("<Left>", self.key_left)
        self.drawer.register_binding("<Right>", self.key_right)
        self.drawer.register_binding("<Key>", self.key)
        # self.drawer.register_binding("<Motion>", self.motion)

    def key_up(self, event):
        self.camera.transposition += np.array([0, 0, 1])

    def key_down(self, event):
        self.camera.transposition += np.array([0, 0, -1])

    def key_left(self, event):
        self.camera.transposition += np.array([-1, 0, 0])

    def key_right(self, event):
        self.camera.transposition += np.array([1, 0, 0])

    def key(self, event):
        camera = self.camera
        if event.char == 'f':
            camera.setF(camera.f + 10)
        elif event.char == 'g':
            camera.setF(camera.f - 10)
        elif event.char == 'q':
            camera.z_angle += 0.1
        elif event.char == 'w':
            camera.z_angle -= 0.1
        elif event.char == 'a':
            camera.y_angle += 0.1
        elif event.char == 's':
            camera.y_angle -= 0.1
        elif event.char == 'z':
            camera.x_angle += 0.1
        elif event.char == 'x':
            camera.x_angle -= 0.1
        elif event.char == 'y':
            camera.transposition += np.array([0, 1, 0])
        elif event.char == 'u':
            camera.transposition += np.array([0, -1, 0])

    mouse_previous_point = None

