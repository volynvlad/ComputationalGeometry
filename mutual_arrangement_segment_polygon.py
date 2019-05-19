from MathHelper import get_intersaction_point as gtp
from MathHelper import param_t_for_line as par_t
from MathHelper import point_from_param_t
from MathHelper import vector1
from MathHelper import scalar
from MathHelper import max2
from MathHelper import min2


def cyrus_beck(p, line):
    assert len(line) == 2
    assert len(line[0]) == 2
    assert len(line[1]) == 2
    a = line[0]
    b = line[1]
    p = p.copy()
    n = len(p)
    p.append(p[0])
    t0 = 0
    t1 = 1
    for i in range(n):
        point = gtp([p[i], p[i + 1]], line)
        temp_t = par_t(a, point, b)
        print("temp_t = ", temp_t)
        n = [-p[i + 1][1] + p[i][1], p[i + 1][0] - p[i][0]]
        ab = [b[0] - a[0], b[1] - a[1]]
        c = scalar(n, ab)
        if c > 0:
            t1 = min2(t1, temp_t)
        elif c < 0:
            t0 = max2(t0, temp_t)
        else:
            print("else")
        print("t0 = %f, t1 = %f" % (t0, t1))
    if t0 > t1:
        return []
    else: # t0 <= t1
        return [point_from_param_t(a, b, t0), point_from_param_t(a, b, t1)]

