import tkinter
from camera_matrix.SolidDraw import SolidDraw


class Drawer:
    frameTime = 30
    offset = (400, 300)

    def __init__(self, projection, height=600, width=800):
        self.projection = projection
        self.topLayer = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.topLayer, bg="white", height=height, width=width)
        self.solidDrawer = SolidDraw(self)
        self.funcs = []
        self.solids = []

    def add_to_loop(self, func):
        self.funcs.append(func)

    def add_solid(self, solid):
        self.solids.append(solid)

    def main_loop(self):
        self.canvas.delete("all")
        self.canvas.pack()

        for func in self.funcs:
            func()

        for solid in self.solids:
            self.solidDrawer.draw(solid)

        self.topLayer.after(self.frameTime, self.main_loop)

    def register_binding(self, key, func):
        self.topLayer.bind(key, func)

    def init(self):
        self.topLayer.after(0, self.main_loop)
        self.topLayer.mainloop()
