from MathHelper import determinant as dt


def is_left(line, point):
    return dt(line[0], line[1], point) < 0


def on_line(line, point):
    return dt(line[0], line[1], point) == 0


def is_right(line, point):
    return dt(line[0], line[1], point) > 0


def is_left(point1, point2, point):
    return dt(point1, point2, point) < 0


def on_line(point1, point2, point):
    return dt(point1, point2, point) == 0


def is_right(point1, point2, point):
    return dt(point1, point2, point) > 0


def point_relative(p1, p2, p):
    """
    p1p2 (l) - line
    p - point
    :param p1:
    :param p2:
    :param p:
    :return: -1 if P left to l
              1 if P right to l
              0 if P on the l
    """
    d = dt(p1, p2, p)
    if d == 0:
        return 0
    else:
        if d > 0:
            return 1
        else:
            return -1
