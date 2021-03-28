import sys
from collections import defaultdict


def fast_count_segments(starts, ends, points):
    """
    https://www.coursera.org/learn/algorithmic-toolbox/discussions/weeks/4/threads/QJ1jK9wNEeWdPBL2iFTrAw/replies/Ihiw4txhEeWK5g7mfcS2Xw/comments/oyAMaeIiEeWyqwpvChh66Q?page=2
    Above approach solve the problem in O(n log n).
    """
    items = []
    for start in starts:
        items.append((start, "l"))
    for end in ends:
        items.append((end, "r"))
    for p in points:
        items.append((p, "p"))

    # Here we pay O(n log n)
    items.sort()

    point_counts = defaultdict(int)
    open_segment: int = 0

    # O(n)
    for item in items:
        if item[1] == "l":
            open_segment += 1
        elif item[1] == "r":
            open_segment -= 1
        else:
            point_counts[item[0]] = open_segment

    return [point_counts[point] for point in points]


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


def simple_solution(starts, ends, points):
    """
    Time compleixty: O(points x len(starts))
    It will stuck at this stage:
        time limit exceeded
    """
    output = [0] * len(points)
    ranges = [slice(start, end) for start, end in zip(starts, ends)]
    for idx, point in enumerate(points):
        for s in ranges:
            if s.start <= point <= s.stop:
                output[idx] = output[idx] + 1
    return output


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2 : 2 * n + 2 : 2]
    ends = data[3 : 2 * n + 2 : 2]
    points = data[2 * n + 2 :]

    results = fast_count_segments(starts, ends, points)

    for r in results:
        print(r, end=" ")
