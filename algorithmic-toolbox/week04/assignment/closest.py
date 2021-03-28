"""
Closest Point problem:
https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer-algorithm/
https://www.youtube.com/watch?v=3pUOv_ocJyA
https://www.youtube.com/watch?v=7tiafUFrlBw
"""
import math
import sys
from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int


def euclidean_distance(p1: Point, p2: Point) -> int:
    xdist = p1.x - p2.x
    ydist = p1.y - p2.y
    return math.sqrt((xdist * xdist) + (ydist * ydist))


def brute_force(points):
    """
    Time complexity: O(n**2)
    space complexity: O(1)
    """
    min_distance = math.inf
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = euclidean_distance(points[i], points[j])
            if distance < min_distance:
                min_distance = distance
    return min_distance


def closest_distance(Px, Py):
    if len(Px) < 4:
        return brute_force(Px)

    # split the data into two halves, according to the median point
    mid: int = len(Px) // 2
    mid_point: Point = Px[mid]

    x_left = Px[:mid]
    x_right = Px[mid:]

    y_left = []
    y_right = []

    for p in Py:
        if p.x < mid_point.x:
            y_left.append(p)
        else:
            y_right.append(p)

    # find the minimum distance on left and right side points
    dl = closest_distance(x_left, y_left)
    dr = closest_distance(x_right, y_right)

    d = min(dl, dr)

    # find points that are at most 2d far from mid_point
    strips = [p for p in Py if mid_point.x - d <= p.x <= mid_point.x + d]
    return min(d, strip_closest(strips, d))


def strip_closest(strips, delta):
    min_distance = delta
    for i in range(len(strips)):
        for j in range(i + 1, min(i + 7, len(strips))):
            distance = euclidean_distance(strips[i], strips[j])
            if distance < min_distance:
                min_distance = distance

    return min_distance


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]

    xs = data[1::2]
    ys = data[2::2]

    points = [Point(x, y) for x, y in zip(xs, ys)]

    Px = sorted(points, key=lambda p: p.x)
    Py = sorted(points, key=lambda p: p.y)

    print("{0:.9f}".format(closest_distance(Px, Py)))
