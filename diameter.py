from MathHelper import length
from MathHelper import triangle_square
from MathHelper import distance
import pdb

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
    #pdb.set_trace()
    max = -1
    k = len(ch)
    ch = ch.copy()
    ch.append(ch[0])
    i = 1
    while triangle_square(ch[k - 1], ch[0], ch[i]) < triangle_square(ch[k - 1],
            ch[0], ch[i + 1]):
        i = i + 1
    start = i
    j = 0
    while True:
        while triangle_square(ch[j], ch[j + 1] , ch[i]) <= triangle_square(ch[j], ch[j + 1], ch[i + 1]) and start < k:
            i = i + 1
        end = i
        a = start
        while a < end:
            if length(ch[a], ch[j]) > max:
                max = length(ch[a], ch[j])
                start = end
                j = j + 1
            a = a + 1
        if i < k and j < k:
            break
    return i, j

