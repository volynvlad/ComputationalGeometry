from ConvexHull import quick_hull
import Triangle
from MathHelper import scalar
from MathHelper import determinant as det
import PointRelative as pR
from IsInSimple import ray_test
from MathHelper import biggest_angle
from MathHelper import start_line
from MathHelper import cos_3points
from MathHelper import point_min
from MathHelper import exists


def is_new_triangular(new_triangle, triangulation):
    for triangle in triangulation:
        if triangle.getPoints() == new_triangle.getPoints():
            return False
    return True
"""
def triangulation_delaunay(triangles, points):
    
    triangles - set of triangles
    new_point - new point
    
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
            if scalar(points[0].get_point(), points[1].get_point()) * scalar(points[0].get_point(), points[2].get_point()) < 0:
                points = [points[1], points[2]]
            elif scalar(points[1].get_point(), points[2].get_point()) * scalar(points[1].get_point(), points[0].get_point()) < 0:
                points = [points[0], points[2]]
            elif scalar(points[2].get_point(), points[0].get_point()) * scalar(points[2].get_point(), points[1].get_point()) < 0:
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
"""

def find(p1, p2, points, tri_sides):
    left_set = []
    for point in points:
        if pR.is_left(p1, p2, point):
            left_set.append(point)
    
    if left_set == []:
        return
    next_p = left_set[0]
    max_angle = 2
    for p in left_set:
        if (cos_3points(p1, p, p2) < max_angle):
            max_angle = cos_3points(p1, p, p2)
            next_p = p

    if exists(p1, p2, p, tri_sides):
        return

    tri_sides.append(p1)
    tri_sides.append(next_p)
    tri_sides.append(next_p)
    tri_sides.append(p2)
    find(p1, next_p, points, tri_sides)
    find(next_p, p2, points, tri_sides)

def delone(tri_sides, points):
    tri_sides.clear()
    p1, p2 = start_line(points)
    tri_sides.append(p1)
    tri_sides.append(p2)
    find(p1, p2, points, tri_sides)


