import math

def determinant(p1, p2, p):
    assert len(p1) == 2
    assert len(p2) == 2
    assert len(p) == 2
    return (p2[0] - p1[0])*(p[1] - p1[1]) - (p2[1] - p1[1])*(p[0] - p1[0])


def length(p1, p2):
    assert len(p1) == 2
    assert len(p2) == 2
    return math.sqrt((p1[0] - p2[0])*(p1[0] - p2[0]) + (p1[1] - p2[1])*(p1[1] - p2[1]))


def angle(p1, p0, p2):
    assert len(p1) == 2
    assert len(p0) == 2
    assert len(p2) == 2
    ca = (p1[0] - p0[0])*(p2[0] - p0[0]) + (p1[1] - p0[1])*(p2[1] - p0[1])
    ca = ca / (length(p1, p0) * length(p2, p0))
    ca = math.acos(ca)
    return ca


def min_and_max(p):
    minimum = p[0]
    maximum = p[0]
    for i in range(len(p)):
        if minimum > p[i]:
            minimum = p[i]
        if maximum < p[i]:
            maximum = p[i]
    return minimum, maximum


def vector1(p1, p2):
    assert len(p1) == 2
    assert len(p2) == 2
    x1 = p1[0]
    x2 = p2[0]
    y1 = p1[1]
    y2 = p2[1]

    return [x2 - x1, y2 - y1]


def point_min(p):
    """
    :param p: points
    :return: max by x and if needed min by y
    """
    minimum = p[0]
    for i in range(len(p)):
        if minimum[1] == p[i][1] and minimum[0] > p[i][0]:
            minimum = p[i]
        if minimum[1] <= p[i][1]:
            minimum = p[i]
    return minimum

def point_min1(p):
    """
    :param p: points
    :return: min by x and if needed min by y
    """
    minimum = p[0]
    for i in range(len(p)):
        if minimum[1] == p[i][1] and minimum[0] < p[i][0]:
            minimum = p[i]
        if minimum[1] <= p[i][1]:
            minimum = p[i]
    return minimum


def point_min_by_x(p):
    """
    p - points
    return - min by x and if needed min by y
    """
    minimum = p[0]
    for i in p:
        if minimum[0] == i[0] and minimum[1] > i[0]:
            minimum = i
        if minimum[0] >= i[0]:
           minimum = i
    return minimum


def point_max_by_x(p):
    """
    p - points
    return - max by x and if needed min by y
    """
    maximum = p[0]
    for i in p:
        if maximum[0] == i[0] and maximum[1] > i[0]:
            maximum = i
        if maximum[0] <= i[0]:
           maximum = i
    return maximum


def oct(v):
    assert len(v) == 2
    x = v[0]
    y = v[1]
    if 0 <= y < x:
        return 1
    if 0 < x <= y:
        return 2
    if 0 <= -x < y:
        return 3
    if 0 < y <= -x:
        return 4
    if 0 <= -y < -x:
        return 5
    if 0 < -x <= -y:
        return 6
    if 0 <= x < -y:
        return 7
    if 0 < -y <= x:
        return 8
    return 0


def cos_num(p1, p2):
    assert len(p1) == 2
    assert len(p2) == 2
    return (p2[0] - p1[0]) / length(p1, p2)


def cos_num_abs(p1, p2):
    assert len(p1) == 2
    assert len(p2) == 2

    return math.fabs(p2[0] - p1[0]) / length(p1, p2)


def scalar(p1, p2):
    assert len(p1) == 2
    assert len(p2) == 2
    return p1[0] * p2[0] + p1[1] * p2[1]


def triangle_square(p1, p2, p3):
    assert len(p1) == 2
    assert len(p2) == 2
    assert len(p3) == 2
    return abs(determinant(p1, p2, p3)) / 2


def perimeter(p):
    sum = 0
    for i in range(len(p)):
        sum = sum + length(p[i - 1], p[i])
    return sum


def distance(p1, p2, p):
    assert len(p1) == 2
    assert len(p2) == 2
    assert len(p) == 2
    A = p1[1] - p2[1]
    B = p2[0] - p1[0]
    C = p1[0] * p2[1] - p2[0] * p1[1]
    return abs(A * p[0] + B * p[1] + C) / math.sqrt(A ** 2 + B ** 2)


def scalar_prod(p1, p2):
    return p1[0] * p2[0] + p1[1] * p2[1]


def gcd(a, b):
    assert a > 0
    assert b > 0
    while b:
        a, b = b, a % b
    return a


def mcd(a, b):
    assert a > 0
    assert b > 0
    return (a / gcd(a, b)) * b


def get_intersaction_point(line1, line2):
    assert len(line1) == 2
    assert len(line2) == 2
    assert len(line1[0]) == 2
    assert len(line1[1]) == 2
    assert len(line2[0]) == 2
    assert len(line2[1]) == 2

    x = []
    y = []

    A1 = line1[1][1] - line1[0][1]
    B1 = line1[0][0] - line1[1][0]
    C1 = -line1[0][0] * line1[1][1] + line1[0][1] * line1[1][0]
    A2 = line2[1][1] - line2[0][1]
    B2 = line2[0][0] - line2[1][0]
    C2 = -line2[0][0] * line2[1][1] + line2[0][1] * line2[1][0]
    if A1 == 0:
        y = line1[0][1]
    if A2 == 0:
        y = line2[0][1]
    if B1 == 0:
        x = line1[0][0]
    if B2 == 0:
        x = line2[0][0]
    if x != [] and y != []: # lines - (horizontal and vertical)
        return x, y
    else:
        if x != []: # one line horizontal
            if B1 == 0:
                return x, -(C2 + A2 * x) / B2
            else:
                return x, -(C1 + A1 * x) / B1
        elif y != []: # one line vertical
            if A1 == 0:
                return -(B2 * y + C2) / A2, y
            else:
                return -(B1 * y + C1) / A1, y
        else: # 2 lines neither vertical not horizontal
            if A1 < 0:
                A1 = -A1
                B1 = -B1
                C1 = -C1
            if A2 < 0:
                A2 = -A2
                B2 = -B2
                C2 = -C2
            A = mcd(A1, A2)
            B1 = B1 * A / A1
            C1 = C1 * A / A1
            A1 = A
            B2 = B2 * A / A2
            C2 = C2 * A / A2
            A2 = A

            y = -(C1 - C2) / (B1 - B2)
            x = -(B1 * y + C1) / A1
            return x, y


def param_t_for_line(start, current, end):
    assert len(start) == 2
    assert len(current) == 2
    assert len(end) == 2

    return length(start, current) / length(start, end)
