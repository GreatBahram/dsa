import math
import sys


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y


def euclidean_distance(p1: Point, p2: Point) -> int:
    xdist = p1.x - p2.x
    ydist = p1.y - p2.y
    return math.sqrt((xdist * xdist) + (ydist * ydist))


def brute_force(points, n):
    min_distance = math.inf
    for i in range(n):
        for j in range(i + 1, n):
            distance = euclidean_distance(points[i], points[j])
            if distance < min_distance:
                min_distance = distance
    return min_distance


def closest_distance(P, Q, n):
    if len(P) < 4:
        return brute_force(P, n)

    # split the data into two halves, according to the median point
    mid: int = n // 2
    mid_point: Point = P[mid]

    dl = closest_distance(P[:mid], Q, mid)
    dr = closest_distance(P[mid:], Q, n - mid)

    d = min(dl, dr)

    strips = [p for p in Q if abs(q.x - mid_point.x) < d]
    return min(d, strip_closest(strips, len(strips), d))


def strip_closest(strips, size, delta):
    min_distance = delta
    for i in range(size):
        for j in range(i + 1, size):
            if (strips[i].y - strips[j].y) < min_distance:
                min_distance = euclidean_distance(strips[i], strips[j])
    return min_distance


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]

    xs = data[1::2]
    ys = data[2::2]

    points = [Point(x, y) for x, y in zip(xs, ys)]

    P = sorted(points, key=lambda p: p.x)
    Q = sorted(points, key=lambda p: p.y)

    print("{0:.9f}".format(minimum_distance(P, Q, n)))
