class SolidDraw:
    def __init__(self, drawer):
        self.drawer = drawer

    def draw(self, solid):
        for edge in solid.edges:
            self.draw_segment_projected(solid.coords[edge[0]], solid.coords[edge[1]])

    def draw_segment_projected(self, A, B):
        offset = self.drawer.offset
        a = self.drawer.projection.localise(A)
        b = self.drawer.projection.localise(B)
        self.drawer.canvas.create_line(a[0] + offset[0], a[1] + offset[1], b[0] + offset[0], b[1] + offset[1])
