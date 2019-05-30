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


def generation_convex_polygon(minimum_x=100, minimum_y=100, maximum_x=700, maximum_y=700, min_points_num=6, max_points_num=7):
    """
    :return: convex polygon: p
    """
    if minimum_x > maximum_x:
        minimum_x, maximum_x = maximum_x, minimum_x
    if minimum_y > maximum_y:
        minimum_y, maximum_y = maximum_y, minimum_y
    x = random.randint(min_points_num, max_points_num)  # number of points in polygon
    p = []
    run = True
    iteration = 0
    while run:
        iteration = iteration + 1
        #  print("iteration: %d | number of points: %d" % (iteration, x))
        p = [[random.randint(minimum_x, maximum_x), random.randint(minimum_y, maximum_y)] for _ in range(x)]

        if is_convex(p):
            # p.clear()
            run = False
    
    max_y = p[0][1]
    max_y_point = p[0]
    for i in p:
        if i[1] > max_y:
            max_y = i[1]
            max_y_point = i

    while p[0] != max_y_point:
        temp_point = p.pop(0)
        p.append(temp_point)

    return p


def generate_random_point(minimum, maximum):
    return [random.randint(minimum, maximum), random.randint(minimum, maximum)]


def generate_random_polygon(minimum, maximum, number):
    result = []
    for i in range(number):
        result.append(generate_random_point(minimum, maximum))

    return result
