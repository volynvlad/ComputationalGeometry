from MathHelper import point_min
from MathHelper import cos_num
import PointRelative as pR
from MathHelper import vector1


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
                cs = cos_num(v1, v2)
                if cs >= max_cos:
                    max_cos = cs
                    p_mc = p[i]
        if p_mc:
            ch.append(p_mc)

    return ch

