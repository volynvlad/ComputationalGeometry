from MathHelper import length
from MathHelper import triangle_square
from MathHelper import distance
import pdb

def slow_diameter(p):
    assert len(p) > 0
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
    assert len(ch) > 0
    result = []
    """
    ch - convex hull
    return:
        indexes of two points
    """
    #pdb.set_trace()
    max = -1
    k = len(ch)
    ch.append(ch[0])
    i = 1
    temp = 0
    while triangle_square(ch[k - 1], ch[0], ch[i + 1]) > triangle_square(ch[k - 1], ch[0], ch[i]):
        i = i + 1
    start = i
    j = 0
    while temp < k:
        temp = start
        while triangle_square(ch[j], ch[j + 1] , ch[temp + 1]) >= triangle_square(ch[j], ch[j + 1], ch[temp]):
           temp = temp + 1
           if temp >= k:
               break
        end = temp
        for a in range(start, end + 1):
            if length(ch[a], ch[j]) > max:
                max = length(ch[a], ch[j])
                result = a, j
        j = j + 1
        start = end
    return result

