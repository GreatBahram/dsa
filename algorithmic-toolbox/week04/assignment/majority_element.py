from collections import Counter


def another_approach(items):
    """Boyer Moore algorithm
    Time complexity: O(n)
    Space complexity: O(1)
    """
    candidate = None
    count = 0
    for item in items:
        if item == candidate:
            count += 1
        elif item != candidate:
            count -= 1
        elif count == 0:
            candidate = item
    return candidate


if __name__ == "__main__":
    n = int(input())
    array = [int(item) for item in input().split()]

    assert n == len(array)

    c = Counter(array)
    first_most_common = c.most_common(1)[0]
    frequency = first_most_common[1]

    if frequency > len(array) / 2:
        print(1)
    else:
        print(0)
