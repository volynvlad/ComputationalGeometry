import PointRelative as pR
import LinesRelative as lR


def convex_point_relative(p, p0):
    assert len(p) > 2
    assert len(p0) == 2
    """
    :param p: polygon
    :param p0: point
    :return:
        True if in polygon
        and 2 points of sector
    """
    start = 0
    end = len(p) - 1
    while end - start > 1:
        sep = (start + end) // 2
        if pR.point_relative(p[0], p[sep], p0) == -1:
            start = sep
        else:
            end = sep
    if pR.point_relative(p[0], p[1], p0) >= 0 or pR.point_relative(p[len(p) - 1], p[0], p0) >= 0:
        return False, p[start], p[end]
    return not lR.is_intersect(p0, p[0], p[start], p[end]), p[start], p[end]
