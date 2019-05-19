import random
from IsSimple import is_simple
from IsConvex import is_convex


def generation_simple_polygon(minimum, maximum):
    """
    :return: simple polygon: p
    """
    x = random.randint(6, 12)  # number of points in polygon
    p = [[]]
    run = True
    iteration = 0
    while run:
        iteration = iteration + 1
        # print("iteration: %d | number of points: %d" % (iteration, x))
        p = [[random.randint(minimum, maximum), random.randint(minimum, maximum)] for _ in range(x)]
        if is_simple(p):
            # p.clear()
            run = False

    return p


def generation_convex_polygon(minimum, maximum):
    """
    :return: convex polygon: p
    """
    x = random.randint(6, 7)  # number of points in polygon
    p = []
    run = True
    iteration = 0
    while run:
        iteration = iteration + 1
        #  print("iteration: %d | number of points: %d" % (iteration, x))
        p = [[random.randint(minimum, maximum), random.randint(minimum, maximum)] for _ in range(x)]

        if is_convex(p):
            # p.clear()
            run = False

    return p


def generate_random_point(minimum, maximum):
    return [random.randint(minimum, maximum), random.randint(minimum, maximum)]


def generate_random_polygon(minimum, maximum, number):
    result = []
    for i in range(number):
        result.append(generate_random_point(minimum, maximum))

    return result
