import PointRelative as pR


def is_convex(p):
    """
    p - polygon | the list of points
    :param p:
    :return: True if p is simple
             False if not
    """
    p = p.copy()
    p.append(p[0])
    p.append(p[1])
    for i in range(len(p)):
        flag = pR.point_relative(p[i], p[i + 1], p[i + 2])
        for x in p:
            if x != p[i] and x != p[i + 1]:
                tmp = pR.point_relative(p[i], p[i + 1], x)
                if flag != 0 and tmp != 0:
                    if flag != tmp:
                        return False
    return True
