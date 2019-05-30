from Draw import draw_arrow
import math
import itertools


class Triangle:
    newid = itertools.count().next
    def __init__(self, points):
        assert len(points) == 3
        self.point1 = p[0]
        if pR.is_left(points[0].get_point(), points[1].get_point(), points[2].get_point()):
                self.point2 = p[1]
                self.point3 = p[2]
            else:
                self.point2 = p[2]
                self.point3 = p[1]

        self.id = resource_cl.newid()
        self.neighbors = []
        print("init triangle - %d" % self.id)


    def draw(self, window, color):
        draw_arrow(window, color, point1, point2)
        draw_arrow(window, color, point2, point3)
        draw_arrow(window, color, point3, point1)
   
   
    def getPoints(self):
       return [self.point1, self.point2, self.point3]

    def getid(self):
        return self.id

    def addneighbor(self, triangle):
        self.neighbors.add(triangle)

    def removeneighborbyid(self, idtriangle):
        k = 0
        for neighbor in self.neighbors:
            count = 0
            if idtriangle == neighbor.getid():
                k = count
            count += 1
        del self.neighbors[k]

    def getneighbors(self):
        return self.neighbors

