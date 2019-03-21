import math
from MathHelper import angle
from MathHelper import min_and_max
from MathHelper import vector1
from MathHelper import determinant as dt
from MathHelper import oct
import PointRelative as pr
import LinesRelative as lr


def gaborit_test(p, p0):
    """
    :param p:
    :param p0:
    :return: False if x < x_min | x > x_max | y < y_min | y > y_max
             x_min if not
    """
    x = [p[i][0] for i in range(len(p))]
    y = [p[i][1] for i in range(len(p))]
    x_min, x_max = min_and_max(x)
    y_min, y_max = min_and_max(y)
    if p0[0] < x_min or p0[0] > x_max or p0[1] < y_min or p0[1] > y_max:
        return False
    return x_min


def ray_test(p, p0):
    """
    :param p: polygon
    :param p0: point
    :return: True if p0 in p
             False if p0 not in p
    """
    is_in_pol = False
    p_tmp = p.copy()
    p_tmp.append(p[0])

    if gaborit_test(p, p0):
        q = gaborit_test(p, p0) - 1, p0[1]
        for i in range(len(p)):
            if lr.is_intersect(p0, q, p_tmp[i], p_tmp[i + 1]):  # if intersect
                if pr.point_relative(p0, q, p_tmp[i]) == 0:  # p[i] on the line p0 q
                    if pr.point_relative(p0, q, p_tmp[i + 1]) == 0:  # line p[i] p[i + 1] is the part of line p0 q
                        if pr.point_relative(p0, q, p_tmp[i - 1]) + pr.point_relative(p0, q, p_tmp[i + 2]) == 0:
                            # p[i - 1] and p[i + 2] on different sides relative to p0 q
                            is_in_pol = not is_in_pol
                            continue
                    else:  # p[i + 1] not on the line p[0] q
                        if pr.point_relative(p0, q, p_tmp[i - 1]) + pr.point_relative(p0, q, p_tmp[i + 1]) == 0:
                            # p[i - 1] and p[i + 1] on one side relative to p0 q
                            is_in_pol = not is_in_pol
                else:  # p[i] not on the line p0 q
                    is_in_pol = not is_in_pol

        return is_in_pol
    else:
        return False


def angle_test(p, p0):
    """
    :param p:
    :param p0:
    :return: true if p0 in p
             false if not
    """
    if gaborit_test(p, p0) is False:
        return False
    s = 0
    p_tmp = p.copy()
    p_tmp.append(p[0])
    for i in range(len(p)):
        ca = angle(p_tmp[i], p0, p_tmp[i + 1])
        if pr.point_relative(p0, p_tmp[i], p_tmp[i + 1]) > 0:
            ca = -ca
        s = ca + s

    if s > math.pi:
        return True
    else:
        return False


def octano_test(p, p0):
    """
    :param p:
    :param p0:
    :return: true if p0 in p
             false if not
    """
    if gaborit_test(p, p0) is False:
        return False
    big_delta = [0 for _ in range(len(p))]
    v1 = [vector1(x, p0) for x in p]
    v2 = v1.copy()
    v2.pop(0)
    v2.append(v1[0])
    s = 0
    for i in range(len(p)):
        delta1 = oct(v1[i - 1])
        delta2 = oct(v2[i - 1])
        big_delta[i] = delta2 - delta1
        if big_delta[i] > 4:
            big_delta[i] = big_delta[i] - 8
        elif big_delta[i] < -4:
            big_delta[i] = big_delta[i] + 8
        elif big_delta[i] == 4 or big_delta[i] == -4:
            d = dt(p[i - 1], p[i], p0)
            if d < 0:
                big_delta[i] = -4
            elif d > 0:
                big_delta[i] = 4
        s = s + big_delta[i]

    if s == 8 or s == -8:
        return True
    elif s == 0:
        return False

