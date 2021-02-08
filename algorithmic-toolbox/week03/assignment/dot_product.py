import sys


if __name__ == "__main__":
    n = map(int, sys.stdin.readline())
    a = map(int, sys.stdin.readline().split())
    b = map(int, sys.stdin.readline().split())
    sorted_a = sorted(a, reverse=True)
    sorted_b = sorted(b, reverse=True)
    max_dot_product = sum(first * second for first, second in zip(sorted_a, sorted_b))
    print(max_dot_product)
