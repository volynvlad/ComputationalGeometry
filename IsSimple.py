import LinesRelative as lr


def is_simple(p):
    """
    p - polygon | the list of points
    :param p:
    :return: True if p is simple
             False if not
    """
    p = p.copy()
    p.append(p[0])
    p.append(p[1])
    for i in range(len(p) - 2):
        for j in range(2, len(p) - 2):
            if p[i] != p[j] and p[i] != p[j + 1] and \
                    p[i + 1] != p[j] and p[i + 1] != p[j + 1] and \
                    lr.is_intersect(p[i], p[i + 1], p[j], p[j + 1]):
                return False
    return True
