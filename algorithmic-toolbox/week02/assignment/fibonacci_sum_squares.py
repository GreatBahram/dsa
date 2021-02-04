PISANO_PERIOD: int = 60


def fibonacci_sum_squares_naive(n: int) -> int:
    if n < 2:
        return n

    previous, next = 0, 1
    last_digits = [previous, next]

    for _ in range(n - 1):
        # We only care about the last digit, so we use modulo 10.
        previous, next = next, (previous + next) % 10
        last_digits.append(next ** 2)

    # make sure we return the last digit.
    return sum(last_digits) % 10


if __name__ == "__main__":
    n = int(input())
    # PISANO_PERIOD makes this algorithm very efficient
    print(fibonacci_sum_squares_naive(n % PISANO_PERIOD))
