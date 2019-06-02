from PointRelative import is_left
from PointRelative import is_right
from LinesRelative import is_intersect
from MathHelper import get_intersection_point
from IsInSimple import ray_test


def is_aim_at(a1, a2, b1, b2):
    d1 = (b2[0] - b1[0]) * (a2[1] - a1[1]) - (b2[1] - b1[1]) * (a2[0] - a1[0])
    d2 = (b2[0] - b1[0]) * (a2[1] - b1[1]) - (b2[1] - b1[1]) * (a2[0] - b1[0])

    if d1 * d2 < 0:
        return True
    if d1 == 0 and d2 == 0:
        sorted_list = sorted_by_x([a1, a2, b1, b2])
        if sorted_list[0] == a2 and sorted_list[1] == a1:
            return False
        elif sorted_list[2] == a1 and sorted_list[3] == a0:
            return False
        else:
            return True
    return False


def outer_window(p, q):
    """
    if True
        p is the outer window to q
    """
    return is_right(p[1], q[0], q[1])


def common_polygon(p, q):
    """
    takes two convex polygons
    returns the intersection polygon
    """
    result = []
    has_intersect = False
    n = len(p)
    m = len(q)
    p = p.copy()
    q = q.copy()
    p.append(p[0])
    q.append(q[0])
    
    i = 0
    j = 0
    while i < n:
        j = 0
        while j < m:
            if is_intersect(p[i], p[i + 1], q[j], q[j + 1]):
                result.append(get_intersection_point([q[j], q[j + 1]], [p[i], p[i + 1]]))
                has_intersect = True
                break
            j += 1
        if has_intersect:
            break
        i += 1
    if not has_intersect:
        return []
    if i != 0:
        p.pop(len(p) - 1)
        new_p = []
        for i_tmp in range(i, len(p)):
            new_p.append(p[i_tmp])
        for i_tmp in range(i):
            new_p.append(p[i_tmp])
        p = new_p.copy()
        p.append(p[0])
    
    if j != 0:
        q.pop(len(q) - 1)
        new_q = []
        for j_tmp in range(j, len(q)):
            new_q.append(q[j_tmp])
        for j_tmp in range(j):
            new_q.append(q[j_tmp])
        q = new_q.copy()
        q.append(q[0])
    
    i = 0
    j = 0
    point = []
    
    while i < n and j < m:
        """
        if ray_test(p, q[j]):
            result.append(q[j])
        if ray_test(p, q[j + 1]):
            result.append(q[j + 1])
        if ray_test(q, p[i]):
            result.append(p[i])
        if ray_test(q, p[i + 1]):
            result.append(p[i + 1])
        """
        ########### 1 ########## and
        if is_aim_at(p[i], p[i + 1], q[j], q[j + 1]) and is_aim_at(q[j], q[j + 1] ,p[i], p[i + 1]): 
            if not outer_window([q[j], q[j + 1]], [p[i], p[i + 1]]):
                result.append(q[j + 1])
                j += 1
                continue
            if not outer_window([p[i], p[i + 1]], [q[j], q[j + 1]]):
                result.append(p[i + 1])
                i += 1
                continue
            else:
                j += 1
                continue
        ########### 2 ########## and not 
        if is_aim_at(p[i], p[i + 1], q[j], q[j + 1]) and not is_aim_at(q[j], q[j + 1] ,p[i], p[i + 1]):
            if not outer_window([p[i], p[i + 1]], [q[j], q[j + 1]]):
                result.append(p[i + 1])
            i += 1
            continue
        ########### 3 ########## not and
        if not is_aim_at(p[i], p[i + 1], q[j], q[j + 1]) and is_aim_at(q[j], q[j + 1] ,p[i], p[i + 1]):
            if not outer_window([q[j], q[j + 1]], [p[i], p[i + 1]]):
                result.append(q[j + 1])
            j += 1
            continue
        ########### 4 ########## not and not
        if not is_aim_at(p[i], p[i + 1], q[j], q[j + 1]) and not is_aim_at(q[j], q[j + 1], p[i], p[i + 1]):
            if is_intersect(p[i], p[i + 1], q[j], q[j + 1]):
                result.append(get_intersection_point([p[i], p[i + 1]], [q[j], q[j + 1]]))
            if outer_window([p[i], p[i + 1]], [q[j], q[j + 1]]):
                i += 1
                continue
            if outer_window([q[j], q[j + 1]], [p[i], p[i + 1]]):
                j += 1
    return result

