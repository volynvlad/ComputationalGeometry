import Generate
from Draw import *
from MathHelper import *
import PointRelative as pR
import LinesRelative as lR
from IsSimple import is_simple
from IsConvex import is_convex
from IsInSimple import *
from ConvexHull import convex_hull
from ConvexHull import jarvis


def main_lab1():
    run = True
    while run:
        print("----------------")
        print("1.Point relative")
        print("2.Lines relative")
        print("3.Simple polygon")
        print("4.Convex polygon")
        print("----------------")
        print("Choose something.(q - quit)")
        x = input()

        if x == '1':
            p1 = Generate.generate_random_point(100, 700)
            p2 = Generate.generate_random_point(100, 700)
            p = Generate.generate_random_point(100, 700)
            point_relative_result = pR.point_relative(p1, p2, p)
            if point_relative_result == 0:
                print("on line")
            else:
                if point_relative_result > 0:
                    print("right")
                else:
                    print("left")
            draw_lab1_1(p1, p2, p)
        elif x == '2':
            p1 = Generate.generate_random_point(100, 700)
            p2 = Generate.generate_random_point(100, 700)
            p3 = Generate.generate_random_point(100, 700)
            p4 = Generate.generate_random_point(100, 700)
            if lR.is_intersect(p1, p2, p3, p4):
                print("intersect")
            else:
                print("don't intersect")
            draw_lab1_2(p1, p2, p3, p4)
        elif x == '3':
            x = random.randint(6, 10)
            p = [Generate.generate_random_point(100, 700) for _ in range(x)]
            if is_simple(p):
                print("simple")
            else:
                print("complex")
            draw_lab1_3(p)
        elif x == '4':
            x = random.randint(6, 10)
            p = [Generate.generate_random_point(100, 700) for _ in range(x)]
            if is_convex(p):
                print("convex")
            else:
                print("concave")
            draw_lab1_4(p)
        elif x == 'q' or x == 'Q':
            run = False
    print("================================")


def main_lab2():
    p = Generate.generation_simple_polygon(100, 700)
    p0 = Generate.generate_random_point(100, 700)
    #  first test
    #############
    #  p = [[200, 400], [400, 200], [600, 400], [400, 600]]
    #  p0 = [300, 400]
    #  second test
    ##############
    #  p = [[100, 200], [200, 200], [400, 100], [300, 400]]
    #  p0 = [300, 200]

    q = gaborit_test(p, p0) - 1, p0[1]

    print("ray test")
    if ray_test(p, p0):
        print("In polygon")
    else:
        print("Not in polygon")

    print("angle test")
    if angle_test(p, p0):
        print("In polygon")
    else:
        print("Not in polygon")

    print("octano test")
    if octano_test(p, p0):
        print("In polygon")
    else:
        print("Not in polygon")
    draw_lab2(p, p0, q)


def main_lab3():
    length = 300
    p = [[random.randint(100, 700), random.randint(100, 700)] for _ in range(length)]
    print("randomed")
    ch = convex_hull(p)

    points = [item for item in p if item not in ch]

    minimum = point_min(points)
    points.remove(minimum)
    for i in range(len(points)):
        for j in range(len(points)):
            if i != j and cos_num(minimum, points[i]) > cos_num(minimum, points[j]):
                points[i], points[j] = points[j], points[i]

    simple_polygon = points[len(points) // 4: 7 + len(points) // 4]

    simple_polygon.append(minimum)

    points = [item for item in points if item not in simple_polygon]

    draw_lab3(ch, points, simple_polygon)


def main_lab4():
    length = 100
    p = [[random.randint(100, 700), random.randint(100, 700)] for _ in range(length)]
    draw_lab4(p)


def main_lab5():
    leng = 100
    p = [[random.randint(100, 700), random.randint(100, 700)] for _ in range(leng)]
    draw_lab5(p)


if __name__ == "__main__":
    print("-------")
    print("|1 lab|")
    print("|2 lab|")
    print("|3 lab|")
    print("|4 lab|")
    print("|5 lab|")
    print("-------")
    print("Choose something.(q - quit)")
    x = input()
    if x == '1':
        main_lab1()
    elif x == '2':
        main_lab2()
    elif x == '3':
        main_lab3()
    elif x == '4':
        main_lab4()
    elif x == '5':
        main_lab5()
