import sys


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

    # copy sorted array from the temp array into the original one
    for idx in range(left, right + 1):
        numbers[idx] = tmp[idx]

    return inversions


def brute_force(array, n):
    inversions = 0
    for i in range():
        for j in range(i + 1, n)):
            if array[j] > array[i]:
                inversions += 1
    return inversions


if __name__ == "__main__":
    input = sys.stdin.read()
    n, *numbers = list(map(int, input.split()))
    # we use this temporary array to save temporarily save the sorted array inside it.
    tmp = n * [0]
    print(get_number_of_inversions(numbers, tmp, 0, n - 1))
