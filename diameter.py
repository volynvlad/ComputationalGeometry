from MathHelper import length
from MathHelper import triangle_square
def slow_diameter(p):
    """
    p - points
    return:
        indexes of two points
    """
    n = len(p)
    i1 = []
    i2 = []
    max = 0
    for i in range(n):
        for j in range(n):
            if length(p[i], p[j]) > max:
                i1 = i
                i2 = j
                max = length(p[i], p[j])

    return i1, i2

def fast_diameter(ch):
    """
    ch - convex hull
    return:
        indexes of two points
    """
    max = -1
    k = len(ch)
    print("length = ", k)
    ch = ch.copy()
    ch.append(ch[0])
    i = 1
    while triangle_square(ch[k - 1], ch[0], ch[i]) < triangle_square(ch[k - 1],
            ch[0], ch[i + 1]):
        i = i + 1
    start = i
    j = 0
    while ch[0] != ch[i]:
        while triangle_square(ch[j], ch[j + 1], ch[start]) <= triangle_square(ch[j], ch[j + 1], ch[start + 1]) and i < k - 1:
            start = start + 1
        end = i
        if triangle_square(ch[start], ch[start + 1], ch[j]) > max:
            max = triangle_square(ch[start], ch[start + 1], ch[j])
            start = end
            j = j + 1
            print("maximum = ", max)

    return i + 1, j

