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

pygame.font.init()
size = [800, 800]

pygame.display.set_caption("Computational Geometry")
clock = pygame.time.Clock()


def draw_lines(p, color, screen):
    for i in range((len(p)) - 1):
        pygame.draw.line(screen, color, p[i], p[i + 1], 5)


def draw_arrow(screen, colour, start, end, coord=False, arrow=False, width=2):
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    dist = 40
    pygame.draw.line(screen, colour, start, end, width)
    rotation = math.degrees(math.atan2(start[1] - end[1], end[0] - start[0])) + 90
    if arrow:
        pygame.draw.polygon(screen, colour,
                            ((end[0] + 12 * math.sin(math.radians(rotation)),
                             end[1] + 12 * math.cos(math.radians(rotation))),
                             (end[0] + 12 * math.sin(math.radians(rotation - 120)),
                              end[1] + 12 * math.cos(math.radians(rotation - 120))),
                             (end[0] + 12 * math.sin(math.radians(rotation + 120)),
                             end[1] + 12 * math.cos(math.radians(rotation + 120)))))
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
        clock.tick(10)
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
        clock.tick(10)
        
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

