import math
import pygame
from IsInSimple import octano_test
from IsInConvex import convex_point_relative
from MathHelper import scalar


class Point:

    def __init__(self, x, y, v_x, v_y):
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y

    def move(self):
        if abs(self.x) > 800:
            self.v_x = 0
        if abs(self.y) > 800:
            self.v_y = 0
        self.x = self.x + self.v_x
        self.y = self.y + self.v_y

    def turn(self, p1, p2):
        """
        b = [p2[0] - p1[0], p2[1] - p1[1]]
        fact = 2 * scalar([self.v_x, self.v_y], b) / scalar(b, b)
        self.v_x = fact * b[0] - self.v_x
        self.v_y = fact * b[1] - self.v_y

        n = [-b[1], b[0]]
        self.v_x = -2 * n[0] * scalar([self.v_x, self.v_y], n) / scalar(n, n) + self.v_x
        self.v_y = -2 * n[1] * scalar([self.v_x, self.v_y], n) / scalar(n, n) + self.v_y
        self.v_x = round(self.v_x)
        self.v_y = round(self.v_y)
        """

        self.v_x = -self.v_x
        self.v_y = -self.v_y

    def draw(self, window, color, width=3):
        pygame.draw.circle(window, color, (round(self.x), round(self.y)), width)

    def convex_collision(self, ch):
        out = convex_point_relative(ch, [self.x + self.v_x,
                                         self.y + self.v_y])

        if not out[0]:
            #  self.v_x = 0
            #  self.v_y = 0
            self.turn(out[1], out[2])

    def simple_collision(self, sh):
        if octano_test(sh, [self.x, self.y]):
            self.v_x = 0
            self.v_y = 0
