from Draw import draw_arrow


class Triangle:
    def __init__(self, points):
        assert len(points) == 3
        self.point1 = points[0]
        self.point2 = points[1]
        self.point3 = points[2]

    def draw(self, window, color):
        draw_arrow(window, color, point1, point2)
        draw_arrow(window, color, point2, point3)
        draw_arrow(window, color, point3, point1)


