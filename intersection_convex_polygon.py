from PointRelative import is_right
from LinesRelative import is_intersect
from MathHelper import get_intersaction_point


def is_look(a1, a2, b1, b2):
    d1 = (b2[0] - b1[0]) * (a2[1] - a1[1]) - (b2[1] - b1[1]) * (a2[0] - a1[0])
    d2 = (b2[0] - b1[0]) * (a2[1] - b1[1]) - (b2[1] - b1[1]) * (a2[0] - b1[0])

    if d1 > 0 and d2 < 0:
        return True
    if d1 < 0 and d2 > 0:
        return True
    return False


def outer_window(p2, q1, q2):
    return is_right(q1, q2, p2)


def common_polygon(p, q):
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
        while j < m:
            if is_intersect(p[i], p[i + 1], q[j], q[j + 1]):
                result.append(get_intersaction_point([p[i], p[i + 1]], [q[j], q[j + 1]]))
                has_intersect = True
                break
            j += 1
        if has_intersect:
            break
        i += 1
    if not has_intersect:
        return []
     
    i = 0
    j = 0
    while i < n and j < m:
        if is_look(p[i], p[i + 1], q[j], q[j + 1]) and is_look(q[j], q[j + 1] ,p[i + 1], p[i]): 
            if outer_window(p[i + 1], q[j], q[j + 1]):
                result.append(p[i + 1])
                i += 1
            else:
                result.append(q[j + 1])
                j += 1
            continue
        #####################
        if is_look(p[i], p[i + 1], q[j], q[j + 1]) and not is_look(q[j], q[j + 1] ,p[i + 1], p[i]):
            if not outer_window(p[i + 1], q[j], q[j + 1]):
                result.append(p[i + 1])
            i += 1
            continue
        #####################
        if not is_look(p[i], p[i + 1], q[j], q[j + 1]) and is_look(q[j], q[j + 1] ,p[i + 1], p[i]):
            if not outer_window(p[i + 1], q[j], q[j + 1]):
                result.append(q[j + 1])
            j += 1
            continue
        #####################
        if not is_look(p[i], p[i + 1], q[j], q[j + 1]) and not is_look(q[j], q[j + 1] ,p[i + 1], p[i]):
            if is_intersect(p[i], p[i + 1], q[j], q[j + 1]):
                result.append(get_intersaction_point([p[i], p[i + 1]], [q[j], q[j + 1]]))
            if outer_window(p[i + 1], q[j], q[j + 1]):
                i += 1
            else:
                j += 1
    print(result)
    return result

