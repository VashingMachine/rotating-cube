class Gui:
    def __init__(self, camera, drawer):
        self.camera = camera
        self.drawer = drawer
        self.drawer.add_to_loop(self.draw_gui)

    def draw_gui(self):
        self.draw_text(str(self.camera.rotation), 200, 30)
        self.draw_text(str(self.camera.transposition), 200, 100)
        self.draw_text(str(self.camera.f), 200, 130)

    def draw_text(self, text, x, y):
        self.drawer.canvas.create_text(x, y, fill="darkblue", font="Times 12 italic bold",
                                       text=text)
