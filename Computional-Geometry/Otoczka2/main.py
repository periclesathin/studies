import numpy as np
import matplotlib.pyplot as plt

def orientacja(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def graham(points):
    n = len(points)

    min_y_index = 0
    for i in range(1, n):
        if points[i][1] < points[min_y_index][1] or (points[i][1] == points[min_y_index][1] and points[i][0] < points[min_y_index][0]):
            min_y_index = i

    points[0], points[min_y_index] = points[min_y_index], points[0]

    p0 = points[0]
    sorted_points = []
    for p in points[1:]:
        angle = np.arctan2(p[1] - p0[1], p[0] - p0[0])
        distance = (p[0] - p0[0])**2 + (p[1] - p0[1])**2
        sorted_points.append((angle, distance, p))

    sorted_points.sort()
    sorted_points = [p for _, _, p in sorted_points]

    hull = [points[0]]
    for p in sorted_points:
        while len(hull) >= 2 and orientacja(hull[-2], hull[-1], p) != 2:
            hull.pop()
        hull.append(p)

    hull += [hull[0]]

    return hull

data = np.loadtxt('ksztalt_1.txt', skiprows=1)
points = data.tolist()

otoczka = graham(points)

plt.scatter(data[:, 0], data[:, 1])

otoczkaX = [p[0] for p in otoczka]
otoczkaY = [p[1] for p in otoczka]

plt.plot(otoczkaX, otoczkaY, 'y-')

plt.show()