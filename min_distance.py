import Point
from MathHelper import sorted_by_x
from MathHelper import sorted_by_y
from MathHelper import length
from MathHelper import min2

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
        return d
    sep = len(X) // 2
    Psep = X[sep]
    XL = X[0 : sep]
    XR = X[sep + 1 : len(X)]
    YL = []
    YR = []
    for i in range(len(X)):
        if X[i][0] > Psep[0]:
            YR.append(X[i])
        if X[i][0] < Psep[0]:
            YL.append(X[i])
    dl = recurtion(XL, YL, result_points)
    dr = recurtion(XR, YR, result_points)
    d = min2(dl, dr)
    Ydel = []
    for i in range(len(Y)):
        if Y[i][0] - Psep[0] < d:
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
    return d

