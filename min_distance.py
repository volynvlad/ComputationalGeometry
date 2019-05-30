import Point
from MathHelper import sorted_by_x
from MathHelper import sorted_by_y
from MathHelper import length
from MathHelper import min2


def slow_min_dist(set_points):
    result_points = []
    result = length(set_points[0], set_points[1])
    for i in range(len(set_points)):
        for j in range(len(set_points)):
            if i != j and length(set_points[i], set_points[j]) < result:
                result_points = set_points[i], set_points[j]
                result = length(set_points[i], set_points[j])

    return result, result_points


def findNearestPairOfPoints(points, result_points):
    points = points.copy() 

    X = sorted_by_x(points)
    Y = sorted_by_y(points)

    return recurtion(X, Y, result_points)

def recurtion(X, Y, result_points):
    if len(X) <= 3:
        d = 1400
        for i in range(len(X)):
            for j in range(len(X)):
                if i != j and length(X[i], X[j]) < d:
                    d = length(X[i], X[j])
                    if len(result_points) != 0:
                        result_points.clear()
                    result_points.append(X[i])
                    result_points.append(X[j])
        return d, result_points
    sep = len(X) // 2
    Psep = X[sep]
    XL = X[0 : sep]
    XR = X[sep : len(X)]
    YL = []
    YR = []
    for i in range(len(Y)):
        if Y[i][0] >= Psep[0]:
            YR.append(Y[i])
        if Y[i][0] < Psep[0]:
            YL.append(Y[i])
    dl, result_points_l = recurtion(XL, YL, result_points)
    dr, result_points_r = recurtion(XR, YR, result_points)
    d = min2(dl, dr)
    if d == dl:
        result_points = result_points_l.copy()
    if d == dr:
        result_points = result_points_r.copy()
    Ydel = []
    for i in range(len(Y)):
        if abs(Y[i][0] - Psep[0]) < d:
            Ydel.append(Y[i])
    for i in range(len(Ydel)):
        j = i
        k = 7
        if len(Ydel) - i < 7:
            k = len(Ydel) - i
        while j < i + k:
            if i != j and length(Ydel[i], Ydel[j]) <= d:
                d = length(Ydel[i], Ydel[j])
                if len(result_points) != 0:
                    result_points.clear()
                result_points.append(Ydel[i])
                result_points.append(Ydel[j])
            j += 1
    return d, result_points.copy()

