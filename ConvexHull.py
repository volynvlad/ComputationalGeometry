from MathHelper import point_min
from MathHelper import cos_num
import PointRelative as pR
from MathHelper import vector1
from MathHelper import cos_num_abs
from MathHelper import length
from MathHelper import point_max_by_x
from MathHelper import point_min_by_x
from MathHelper import triangle_square

import math

def convex_hull(p):
    ch = []

    p = p.copy()
    s0 = point_min(p)
    p.remove(s0)
    for i in range(len(p)):
        for j in range(len(p)):
            if i != j and cos_num(s0, p[i]) > cos_num(s0, p[j]):
                p[i], p[j] = p[j], p[i]
    print("sorted")
    ch.append(s0)
    ch.append(p[0])

    p.remove(p[0])
    for i in range(len(p)):
        # print(pr.point_relative(s0, p[0], p[i]))
        while len(ch) != 2 and not pR.is_left(ch[-2], ch[-1], p[i]):
            ch.pop()
        ch.append(p[i])

    return ch


def convex_hull_step_by_step(p):
    result = []
    ch = []

    p = p.copy()
    s0 = point_min(p)
    p.remove(s0)
    for i in range(len(p)):
        for j in range(len(p)):
            if i != j and cos_num(s0, p[i]) > cos_num(s0, p[j]):
                p[i], p[j] = p[j], p[i]
    print("Points was sorted")
    p.append(s0)
    ch.append(s0)
    start_point = p[0]
    ch.append(start_point)
    ch_copy = ch.copy()
    result.append(ch_copy)

    p.remove(start_point)
    for i in range(len(p)):
        while len(ch) != 2 and not pR.is_left(ch[-2], ch[-1], p[i]):
            ch.pop()
            ch_copy = ch.copy()
            result.append(ch_copy)
        ch.append(p[i])
        ch_copy = ch.copy()
        result.append(ch_copy)
    return result


def jarvis(p):
    s0 = point_min(p)
    ch = []
    ch.append(s0)
    p = p.copy()

    p_mc = 1
    while p_mc:
        max_cos = -1
        p_mc = []
        p0 = ch[-1]
        for i in range(len(p)):
            v1 = vector1(p0, [p0[0] + 1, p0[1]])
            v2 = vector1(p0, p[i])
            if pR.point_relative(p0, [p0[0] + 1, p0[1]], p[i]) == -1:
                cs = cos_num(v1, v2)
                if cs >= max_cos:
                    max_cos = cs
                    p_mc = p[i]
        if p_mc:
            ch.append(p_mc)

    p_mc = 1
    while p_mc:
        max_cos = -1
        p_mc = []
        p0 = ch[-1]
        for i in range(len(p)):
            v1 = vector1(p0, [p0[0] - 1, p0[1]])
            v2 = vector1(p0, p[i])
            if pR.point_relative(p0, [p0[0] - 1, p0[1]], p[i]) == -1:
                cs = cos_num(v2, v1)
                if cs >= max_cos:
                    max_cos = cs
                    p_mc = p[i]
        if p_mc:
            ch.append(p_mc)
    ch.pop()
    return ch

def far_point(p1, p2, set):
    """
    p1, p2 - line 
    set - points
    return
        most far point in set from p1 p2
    """
    far_p = []
    max = 0
    for x in set:
        if triangle_square(p1, p2, x) > max:
            max = triangle_square(p1, p2, x)
            far_p = x
    return far_p


def quick_hull(p):
    s_l = []
    s_r = []
    ch = []
    p_l = point_min_by_x(p)
    p_r = point_max_by_x(p)
    for x in p:
        if pR.is_left(p_l, p_r, x):
            s_l.append(x)
        if pR.is_right(p_l, p_r, x):
            s_r.append(x)
    ch.append(p_l)
    ch.append(p_r)
    iter_hull(s_l, p_l, p_r, ch)
    iter_hull(s_r, p_r, p_l, ch)
    ch.append(p_l)
    return ch


def iter_hull(points, left, right, ch):
    sl = []
    
    for x in points:
        if pR.is_left(left, right, x):
            sl.append(x)

    if sl:
        lrp = far_point(right, left, sl)
        ch.insert(ch.index(left) + 1, lrp)
        iter_hull(sl, left, lrp, ch)
        iter_hull(sl, lrp, right, ch)



