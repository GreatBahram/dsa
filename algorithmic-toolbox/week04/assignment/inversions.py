import sys


def count_inversions(numbers):
    """
    >>> items = [8, 4, 2, 1]
    >>> count_inversions(items)
    6
    """
    tmp = [0] * len(numbers) 
    return get_number_of_inversions(numbers, tmp, 0, len(numbers) - 1)


def get_number_of_inversions(numbers, tmp, left, right) -> int:
    inversions = 0

    if left < right:
        mid = (left + right) // 2

        inversions += get_number_of_inversions(numbers, tmp, left, mid)
        inversions += get_number_of_inversions(numbers, tmp, mid + 1, right)

        inversions += merge(numbers, tmp, left, mid, right)

    return inversions


def merge(numbers, tmp, left, mid, right):
    i = k = left
    j = mid + 1
    inversions = 0

    while i <= mid and j <= right:
        if numbers[i] <= numbers[j]:
            tmp[k] = numbers[i]
            i += 1
            k += 1
        else:
            # inversion will occur here
            tmp[k] = numbers[j]
            j += 1
            k += 1
            inversions += mid - i + 1

    while i <= mid:
        tmp[k] = numbers[i]
        i += 1
        k += 1

    while j <= right:
        tmp[k] = numbers[j]
        j += 1
        k += 1

    for idx in range(left, right + 1):
        numbers[idx] = tmp[idx]

    return inversions


if __name__ == "__main__":
    input = sys.stdin.read()
    n, *numbers = list(map(int, input.split()))
    tmp = n * [0]
    print(get_number_of_inversions(numbers, tmp, 0, n - 1))
