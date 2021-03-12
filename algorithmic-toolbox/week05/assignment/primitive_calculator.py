from typing import Dict, List


def optimal_sequence(n):
    """Greedy approach."""
    sequence = [n]
    while n >= 1:
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
        sequence.append(n)
    return reversed(sequence)


def pcalc(n: int) -> int:
    memo = {1: 0, 2: 1, 3: 1}

    if n in memo:
        return memo[n]

    for i in range(4, n + 1):
        memo[i] = memo[i - 1] + 1
        memo[i] = min(
            memo[i],
            memo[i // 3] + 1
            if i % 3 == 0
            else memo[(i - 1) // 3] + 2
            if i % 3 == 1
            else memo[(i - 2) // 3] + 3,
        )
        memo[i] = min(
            memo[i], memo[i // 2] + 1 if i % 2 == 0 else memo[(i - 1) // 2] + 2
        )
    return memo[n]


def find_sequence(n: int, mapping: Dict[int, int]) -> List[int]:
    sequence = [n]
    while n > 1:
        value = 0
        value_3 = mapping[n // 3] if n % 3 == 0 else n
        value_2 = mapping[n // 2] if n % 2 == 0 else n
        value_1 = mapping[n - 1]

        if value_3 <= min(value_2, value_1):
            value = n // 3
        elif value_2 <= min(value_3, value_1):
            value = n // 2
        else:
            value = n - 1
        n = value
        sequence.append(n)
    return reversed(sequence)


def primitive_calc(n: int):
    memo = {1: 0, 2: 1, 3: 1}

    for i in range(4, n + 1):
        count_3 = count_2 = count_1 = n
        if i % 3 == 0:
            count_3 = memo[i // 3]
        if i % 2 == 0:
            count_2 = memo[i // 2]
        if i - 1 >= 0:
            count_1 = memo[i - 1]
        memo[i] = min(count_3, count_2, count_1) + 1

    return memo[n], find_sequence(n, memo)


if __name__ == "__main__":
    n = int(input())
    operations_num, sequence = primitive_calc(n)
    print(operations_num)
    for x in sequence:
        print(x, end=" ")
    print()
