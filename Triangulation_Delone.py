from ConvexHull import quick_hull
import Triangle
from MathHelper import scalar_prod, det 
import PointRelative as pR


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
        
