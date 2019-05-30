from ConvexHull import quick_hull
import Triangle
from MathHelper import scalar_prod, det 
import PointRelative as pR
from IsInSimple import ray_test


def triangulation_delaunay(triangles, points):
    """
    triangles - set of triangles
    new_point - new point
    """
    if len(points) == 0:
        return []
    elif len(points) == 1:
        return points
    elif len(points) == 2:
        if points[0].get_point() == points[1].get_point():
            points = points[0]
    elif len(points) == 3:
        if (points[2].get_point() == points[0].get_point() or points[2].get_point() == points[1].get_point()) and points[0].get_point() != points[1].get_point():
            points = [points[0], points[1]]
        if points[0].get_point() == points[1].get_point() and points[0].get_point() == points[2].get_point():
            points = points[0]
        if det(points[0].get_point(), points[1].get_point(), points[2].get_point()) == 0:
            if scalar_prod(points[0].get_point(), points[1].get_point()) * scalar_prod(points[0].get_point(), points[2].get_point()) < 0:
                points = [points[1], points[2]]
            elif scalar_prod(points[1].get_point(), points[2].get_point()) * scalar_prod(points[1].get_point(), points[0].get_point()) < 0:
                points = [points[0], points[2]]
            elif scalar_prod(points[2].get_point(), points[0].get_point()) * scalar_prod(points[2].get_point(), points[1].get_point()) < 0:
                points = [points[0], points[1]]
            else:
                triangle.add([points[0], points[1], points[2]])
    else:
        last_point = points[-1]
        temp_triangles = []
        side_points = []
        triangle_points = []
        for triangle in triangles:
            if ray_test(triangle.getPoints(), last_point):
                temp_triangles.add(triangle)
       
        if temp_triangles != []:

            for i in range(3):
                if pR.on_line(temp_triangles.getPoints()[i - 1], temp_triangles.getPoints()[i], last_point) and last_point not in temp_triangles.getPoints():
                    side_points = [temp_triangles.getPoints()[i - 1], temp_triangles.getPoints()[i]]

            if side_points == []:
                triangle_points = temp_triangles.getPoints()
                for neighbor in temp_triangles.getneighbors():
                    neighbor.removeneighborbyid(temp_triangles.getid())
            
                for i in len(triangles):
                    if triangles[i].getid() == temp_triangles[0]:
                        del triangles[i]

                for i in range(3):
                    new_triangle = Triangle.Triangle([temp_triangles[0].getPoints()[i - 1], temp_triangles[0].getPoints()[i], last_point])
                    triangles.add(new_triangle)
                    for neighbor in temp_triangles[0].getneighbors():
                        if temp_triangles[0].getPoints()[i - 1] in neighbor.getPoints() and temp_triangles[0].getPoints()[i] in neighbor.getPoints():
                            neighbor.addneighbor(new_triangle)

