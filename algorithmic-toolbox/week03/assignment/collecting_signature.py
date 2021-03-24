from typing import List, NamedTuple


class Segment(NamedTuple):
    start: int
    end: int


def optimal_points(segments: List[Segment]):
    points = []

    sorted_by_ends = sorted(segments, key=lambda s: s.end)
    current = sorted_by_ends[0].end
    points.append(current)

    for segment in sorted_by_ends[1:]:
        if current < segment.start or current > segment.end:
            current = segment.end
            points.append(current)
    return points


if __name__ == "__main__":
    import sys

    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
