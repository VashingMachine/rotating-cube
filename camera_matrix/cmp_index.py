from camera_matrix.CameraMatrixProjection import CameraProjection
from camera_matrix.Drawer import Drawer
from camera_matrix.solids.Cuboid import Cuboid
from camera_matrix.CameraController import Controller
from camera_matrix.CameraGui import Gui
import numpy as np

projection = CameraProjection(400)
drawer = Drawer(projection)
controller = Controller(projection, drawer)
gui = Gui(projection, drawer)

drawer.add_solid(Cuboid(np.array([0, 0, 200]), 100, 100, 100))
drawer.add_solid(Cuboid(np.array([0, 0, 300]), 100, 100, 100))
drawer.add_solid(Cuboid(np.array([200, 0, 300]), 50, 80, 100))
drawer.add_solid(Cuboid(np.array([200, 200, 300]), 100, 100, 100))

drawer.init()
