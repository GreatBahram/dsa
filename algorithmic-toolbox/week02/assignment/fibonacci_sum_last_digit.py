PISANO_PERIOD: int = 60


def fibonacci_sum(n: int) -> int:
    """
    Find the last digit of a sum of the first n Fibonacci numbers.
    """
    if n < 2:
        return n

    n -= 1
    previous = 0
    current = 1
    sum = 1

    for _ in range(n % PISANO_PERIOD):
        previous, current = current, (previous + current) % 10
        sum += current

    return sum % 10 - 1


if __name__ == "__main__":
    n = int(input())
    print(fibonacci_sum(n))
