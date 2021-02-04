PISANO_PERIOD: int = 60


def fib_last_digit(n: int) -> int:
    """
    Fibonacci numbers repeats with a cycle length of 60.
    """
    if n == 0:
        return n

    a, b = 0, 1

    for _ in range(n % PISANO_PERIOD):
        a, b = b, (a + b) % 10
    return a


if __name__ == "__main__":
    n = int(input())
    print(fib_last_digit(n))
