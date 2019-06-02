import Generate
import pygame
import random
import math
import Point
from color import *
from ConvexHull import *
from diameter import slow_diameter
from diameter import fast_diameter
from MathHelper import perimeter
from ConvexHull import dynamic_convex_hull
from mutual_arrangement_segment_polygon import cyrus_beck
from min_distance import findNearestPairOfPoints
from min_distance import slow_min_dist
from intersection_convex_polygon import common_polygon
from Triangulation_Delone import delone
import Vector3D
import Point3D
import Quanterion
import Cube



pygame.font.init()
size = [800, 800]

pygame.display.set_caption("Computational Geometry")
clock = pygame.time.Clock()


def draw_lines(p, color, screen):
    for i in range((len(p)) - 1):
        pygame.draw.line(screen, color, p[i], p[i + 1], 5)


def draw_arrow(screen, colour, start, end, coord=False, arrow=False, width=2):
    rot_num = 100
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    dist = 40
    pygame.draw.line(screen, colour, start, end, width)
    rotation = math.degrees(math.atan2(start[1] - end[1], end[0] - start[0])) + 90
    if arrow:
        pygame.draw.polygon(screen, colour,
                            ((end[0] + 12 * math.sin(math.radians(rotation)),
                             end[1] + 12 * math.cos(math.radians(rotation))),
                             (end[0] + 12 * math.sin(math.radians(rotation -
                                 rot_num)),
                              end[1] + 12 * math.cos(math.radians(rotation -
                                  rot_num))),
                             (end[0] + 12 * math.sin(math.radians(rotation +
                                 rot_num)),
                             end[1] + 12 * math.cos(math.radians(rotation +
                                 rot_num)))))
    text_start = my_font.render("(%d, %d)" % (start[0], start[1]), False, BLACK)
    text_end = my_font.render("(%d, %d)" % (end[0], end[1]), False, BLACK)
    if coord:
        screen.blit(text_start, (start[0], start[1] - dist))
        screen.blit(text_end, (end[0], end[1] - dist))


def draw_lab1_1(p1, p2, p):
    pygame.init()
    window = pygame.display.set_mode(size)
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.fill(WHITE)

        draw_arrow(window, BLACK, (400, 0), (400, 790), False, True)
        draw_arrow(window, BLACK, (0, 400), (790, 400), False, True)
        draw_arrow(window, RED, p1, p2, False, True)
        "pygame.draw.line(screen, RED, p1, p2, 5)"
        pygame.draw.circle(window, BLUE, p, 4)
        pygame.display.flip()

    pygame.quit()


def draw_lab1_2(p1, p2, p3, p4):
    pygame.init()
    window = pygame.display.set_mode(size)
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.fill(WHITE)

        draw_arrow(window, BLACK, (400, 0), (400, 790), False, True)
        draw_arrow(window, BLACK, (0, 400), (790, 400), False, True)
        draw_arrow(window, RED, p1, p2, False, True)
        draw_arrow(window, RED, p3, p4, False, True)
        pygame.display.flip()

    pygame.quit()


def draw_lab1_3(p):
    pygame.init()
    window = pygame.display.set_mode(size)
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.fill(WHITE)

        for i in range(len(p)):
            draw_arrow(window, RED, p[i - 1], p[i], False, True)
        pygame.display.flip()

    pygame.quit()


def draw_lab1_4(p):
    window = pygame.display.set_mode(size)
    pygame.init()
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.fill(WHITE)

        for i in range(len(p)):
            draw_arrow(window, RED, p[i - 1], p[i], False, True)
        pygame.display.flip()

    pygame.quit()


def draw_lab2(p, p0, q):
    pygame.init()
    window = pygame.display.set_mode(size)
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.fill(WHITE)
        for i in range(len(p)):
            draw_arrow(window, RED, p[i - 1], p[i], True)

        pygame.draw.circle(window, BLUE, p0, 3)
        draw_arrow(window, BLACK, p0, q)

        pygame.display.flip()
    pygame.quit()


def draw_lab3(ch, points, simple_polygon):
    points_move = []
    window = pygame.display.set_mode(size)
    pygame.init()
    for i in range(len(points)):
        points_move.append(Point.Point(points[i][0], points[i][1], random.randint(-5, 5), random.randint(-5, 5)))

    clock = pygame.time.Clock()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        clock.tick(20)
        window.fill(WHITE)

        pygame.draw.polygon(window, BLUE, simple_polygon)

        for point_move in points_move:
            point_move.draw(window, BLACK)
            point_move.move(size)
            point_move.convex_collision(ch)
            point_move.simple_collision(simple_polygon)

        for i in range(len(ch)):
            #  pygame.draw.line(window, RED, ch[i - 1], ch[i], 2)
            draw_arrow(window, RED, ch[i - 1], ch[i])

        pygame.display.flip()

    pygame.quit()


def draw_lab4(p):
    pygame.display.set_caption('Cartoon')
    window = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    lines = convex_hull_step_by_step(p)
    for line in lines:
        print(line)

    i = -1
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.fill(WHITE)

        clock.tick(50)
        if i < len(lines) - 1:
            i = i + 1
        else:
            i = 0
        draw_lines(lines[i], RED, window)

        for x in p:
            pygame.draw.circle(window, BLACK, x, 3)

        pygame.display.flip()

    pygame.quit()


def draw_lab5(p):
    points_move = []
    chs_move = []
    n = len(p)
    pygame.display.set_caption('Cartoon')
    window = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    for i in p:
        points_move.append(Point.Point(i[0], i[1],
            random.randint(1, 2) * (-1)
            ** random.randint(0, 1),
            random.randint(1, 2) * (-1)
            ** random.randint(0, 1)))

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.fill(WHITE)
        clock.tick(60)
        ch = jarvis(p)
        for i in range(len(points_move)):
            points_move[i].draw(window, BLACK)
            points_move[i].move(size)
            p[i] = points_move[i].get_point()


        for i in range(len(ch)):
            draw_arrow(window, RED, [ch[i - 1][0], ch[i - 1][1]],
                    [ch[i][0],ch[i][1]], width = 3)


        i1, i2 = slow_diameter(p)
        draw_arrow(window, GREEN, p[i1], p[i2], width = 4)
        i3, i4 = fast_diameter(ch)
        draw_arrow(window, BLUE, ch[i3], ch[i4], width = 4)

        points_move[i1].set_speed(-points_move[i1].v_x, -points_move[i1].v_y)
        points_move[i2].set_speed(-points_move[i2].v_x, -points_move[i2].v_y)
        pygame.display.flip()

    pygame.quit()


def draw_lab6(p):
    points_move = []
    chs_move = []

    n = len(p)
    pygame.display.set_caption('Cartoon')
    window = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    for i in p:
        points_move.append(Point.Point(i[0], i[1],
            random.randint(1, 2) * (-1)
            ** random.randint(0, 1),
            random.randint(1, 2) * (-1)
            ** random.randint(0, 1)))

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.fill(WHITE)
        clock.tick(30)

        for i in range(len(points_move)):
            points_move[i].move(size)
            p[i] = points_move[i].get_point()
            points_move[i].draw(window, BLACK)

        ch = quick_hull(p)

        for i in range(len(ch)):
            draw_arrow(window, RED, [ch[i - 1][0], ch[i - 1][1]],
                    [ch[i][0],ch[i][1]], width = 3)
        print(perimeter(ch))
        if perimeter(ch) > 2300:
            for x in ch:
                index = p.index(x)
                points_move[index].set_speed(-points_move[index].v_x,
                        -points_move[index].v_y)

        pygame.display.flip()

    pygame.quit()

def draw_lab7():
    p = []
    ch = []
    pygame.display.set_caption('Cartoon')
    window = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                point = Point.Point(pos[0], pos[1], 0, 0)
                point = point.__copy__()
                p.append(point)
                ch = dynamic_convex_hull(p, ch)

        window.fill(WHITE)
        clock.tick(30)

        if ch != []:
            for i in range(len(ch)):
                draw_arrow(window, RED, [ch[i - 1].get_point()[0], ch[i -
                    1].get_point()[1]],
                        [ch[i].get_point()[0], ch[i].get_point()[1]], width = 3)
        for i in range(len(p)):
            p[i].draw(window, BLACK)
            p[i].move(size)

        pygame.display.flip()

    pygame.quit()

def draw_lab8(p, lines):
    pygame.display.set_caption('Cartoon')
    window = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    cuted_lines = []
    for line in lines:
        cuted_line = cyrus_beck(p, line)
        if cuted_line != []:
            cuted_lines.append(cuted_line)
    print("cuted lines", cuted_lines)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.fill(WHITE)
        clock.tick(30)

        for i in range(len(p)):
            draw_arrow(window, BLACK, p[i - 1], p[i], width=3)
        for line in lines:
            draw_arrow(window, RED, line[0], line[1], arrow=True)
        for cuted_line in cuted_lines:
            draw_arrow(window, BLUE, cuted_line[0], cuted_line[1])

        pygame.display.flip()

    pygame.quit()

def draw_lab9(p, q):
    pygame.display.set_caption('Cartoon')
    window = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    my_font = pygame.font.SysFont('Comic Sans MS', 30)

    points_p = []
    points_q = []
    points_g = []
    cur_points_p = [[0, 0] for _ in range(len(p))]
    cur_points_q = [[0, 0] for _ in range(len(q))]

    for i in p:
        points_p.append(Point.Point(i[0], i[1], 1, 0))
    for i in q:
        points_q.append(Point.Point(i[0], i[1], -1, 0))

    pause = False 

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                pause = not pause

        window.fill(WHITE)
        if pause:
            clock.tick(0)
            continue
        else:
            clock.tick(30)

        pygame.draw.polygon(window, RED, cur_points_p)
        pygame.draw.polygon(window, GREEN, cur_points_q)


        for i in range(len(points_p)):
            #points_p[i].draw(window, BLACK)
            points_p[i].move(size)
            cur_points_p[i] = points_p[i].get_point()
            text_start = my_font.render("%d" % (i), False, BLUE)
            window.blit(text_start, (points_p[i].get_point()[0], points_p[i].get_point()[1]))

       
        for i in range(len(points_q)):
            #points_q[i].draw(window, BLACK)
            points_q[i].move(size)
            cur_points_q[i] = points_q[i].get_point()
            text_start = my_font.render("%d" % (i), False, BLACK)
            window.blit(text_start, (points_q[i].get_point()[0], points_q[i].get_point()[1]))
    
        if len(cur_points_p) > 2 and len(cur_points_q) > 2:
            common_points = common_polygon(cur_points_p, cur_points_q)
        if len(common_points) > 0:
            common_points = jarvis(common_points)
        if len(common_points) > 2:
            pygame.draw.polygon(window, BLUE, common_points)
        for i in common_points:
            points_g.append(Point.Point(i[0], i[1], 1, 0))

        for i in points_g:
            i.draw(window, BLACK)

        points_g.clear()

        pygame.display.flip()

    pygame.quit()
 

def draw_lab10(p):
    points_move = []
    pygame.display.set_caption('Cartoon')
    window = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    for i in p:
        points_move.append(Point.Point(i[0], i[1], 0, 0))
    result = []
    print("Slow")
    print(slow_min_dist(p))
    print("Fast")
    print(findNearestPairOfPoints(p, result))
    print("difference - ", slow_min_dist(p)[0] - findNearestPairOfPoints(p, result)[0])
    T = True
    for i in findNearestPairOfPoints(p, result)[1]:
        if i not in slow_min_dist(p)[1]:
            T = False
    for i in slow_min_dist(p)[1]:
        if i not in findNearestPairOfPoints(p, result)[1]:
            T = False
    if T:
        print("same points")
    else:
        print("different point")
    result = findNearestPairOfPoints(p, result)[1]
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.fill(WHITE)
        clock.tick(30)

        draw_arrow(window, BLACK, result[0], result[1], width=3)

        for i in range(len(points_move)):
            points_move[i].draw(window, BLACK)

        pygame.display.flip()

    pygame.quit()

def draw_lab11():

    points = []
    sides = []


    pygame.display.set_caption('Cartoon')
    window = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    run = True
    while run:
        window.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                pos = list(pos)
                points.append(pos)
        if len(points) > 2:
            delone(sides, points)
            sides.append(sides[0])
        for i in range(0, len(sides) - 1):
            draw_arrow(window, RED, sides[i], sides[i + 1])
        if sides != []:
            sides.remove(sides[len(sides) - 1]) 

        for point in points:
            pygame.draw.circle(window, BLACK, (point[0], point[1]), 2)

        clock.tick(30)


        pygame.display.flip()

    pygame.quit()

def draw_lab12():

    cube = []
    cent_point = []
    rot_vector = []

    v1 = Vector3D.Vector3D(0, 50, 0)
    v2 = Vector3D.Vector3D(50, 0, 0)
    p = Point3D.Point3D(100, 100, 200)
    print(p)
    print(v1)
    print(v2)
    cube = Cube.Cube(p, v1, v2, 40)
    cent_point = Point3D.Point3D(0, 0, 100)
    rot_vector = Vector3D.Vector3D(15, 20, 50)
    lines = []
    pygame.display.set_caption('Cartoon')
    window = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    run = True
    while run:

        window.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        cube_sides = cube.get_sides()
        for cube_side in cube_sides:
            x1 = (cube_side[0].x * cent_point.z - cube_side[0].z * cent_point.x) / (cent_point.z - cube_side[0].z)
            y1 = (cube_side[0].y * cent_point.z - cube_side[0].z * cent_point.y) / (cent_point.z - cube_side[0].z)
            x2 = (cube_side[1].x * cent_point.z - cube_side[1].z * cent_point.x) / (cent_point.z - cube_side[1].z)
            y2 = (cube_side[1].y * cent_point.z - cube_side[1].z * cent_point.y) / (cent_point.z - cube_side[1].z)
        
            lines.append([[x1, y1], [x2, y2]])

        for line in lines:
            draw_arrow(window, BLACK, line[0], line[1], 2)
        
        lines.clear()

        cube.rotate(rot_vector)


        clock.tick(3)

        pygame.display.flip()

    pygame.quit()
