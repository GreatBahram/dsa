import sys

PISANO_PERIOD: int = 60


def fibonacci_partial_sum_naive(from_: int, to: int) -> int:
    """
    Find the last digit of a partial sum of Fibonacci numbers: Fm + Fm+1 + ··· + Fn.
    """
    sum = 0
    current = 0
    next = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, (current + next) % 10

    return sum % 10


if __name__ == "__main__":
    input = sys.stdin.read()
    from_, to = map(int, input.split())

    # The Pisano_period produces a huge performance improvement
    from_, to = from_ % PISANO_PERIOD, to % PISANO_PERIOD

    # https://codereview.stackexchange.com/a/171988/220025
    if to < from_:
        to += PISANO_PERIOD

    print(fibonacci_partial_sum_naive(from_, to))
