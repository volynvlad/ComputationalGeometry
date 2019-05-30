from MathHelper import determinant as dt


def is_same(p):
    tmp = []
    for i in p:
        if tmp.__contains__(i):
            return True
        else:
            tmp.append(i)
    return False


def is_intersect(p1, p2, p3, p4):
    assert len(p1) == 2
    assert len(p2) == 2
    assert len(p3) == 2
    assert len(p4) == 2
    """
    p1p2 (l1) - line
    p3p4 (l2) - line
    :param p1:
    :param p2:
    :param p3:
    :param p4:
    :return: True if l1 and l2 have same point(points)
             False if not
    """

    d1 = dt(p3, p4, p1)
    d2 = dt(p3, p4, p2)
    d3 = dt(p1, p2, p3)
    d4 = dt(p1, p2, p4)

    p = [p1, p2, p3, p4]
    tmp1 = []
    x = [p[i][0] for i in range(4)]
    y = [p[i][1] for i in range(4)]

    if d1 != 0 or d2 != 0 or d3 != 0 or d4 != 0:
        if d1 * d2 <= 0 and d3 * d4 <= 0:
            return True
        else:
            return False
    else:
        if is_same(p):  # line and point
            return True
        elif p1[0] == p2[0] and p1[0] == p3[0] and p1[0] == p4[0]:  # x equals
            for i in range(len(y)):
                tmp1 = []
                tmp2 = y.copy()
                min_y_p = min(y)
                tmp1.append(min_y_p)
                tmp2.remove(min_y_p)
                min_y_p = min(tmp2)
                tmp1.append(min_y_p)
            if [p1[1], p2[1]].sort() == tmp1.sort() or [p3[1], p4[1]].sort() == tmp1.sort():
                return False
            else:
                return True
        elif p1[1] == p2[1] and p1[1] == p3[1] and p1[1] == p4[1]:  # y equals
            for i in range(len(x)):
                tmp2 = x.copy()
                min_x_p = min(x)
                tmp1.append(min_x_p)
                tmp2.remove(min_x_p)
                min_x_p = min(tmp2)
                tmp1.append(min_x_p)
            if [p1[0], p2[0]].sort() == tmp1.sort() or [p3[0], p4[0]].sort() == tmp1.sort():
                return False
            else:
                return True
        else:  # in formula l: y = k*x + b; k equals
            for i in range(len(y)):
                tmp1 = []
                tmp2 = y.copy()
                min_y_p = min(y)
                tmp1.append(min_y_p)
                tmp2.remove(min_y_p)
                min_y_p = min(tmp2)
                tmp1.append(min_y_p)
            if [p1[1], p2[1]].sort() == tmp1.sort() or [p3[1], p4[1]].sort() == tmp1.sort():
                return False
            else:
                return True
