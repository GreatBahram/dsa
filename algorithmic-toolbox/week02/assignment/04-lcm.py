def euclidean_approach(num1: int, num2: int) -> int:
    """
    Mathematical proof of this apporach can be found here:
    https://www.youtube.com/watch?v=H_2_nqKAZ5w

    In this implementation we assumed num1 is always bigger than num2.
    And the recursive approach is chosen as it is easier to read. However,
    below you can find non-recursive implementation:

    def euclidean_approach(num1, num2):
        while num2:
            num1, num2 = num2, num1 % num2
        return num1
    """
    if num1 == num2:
        return num1

    if num2 == 0:
        return num1

    return euclidean_approach(num2, num1 % num2)


def lcm(num1: int, num2: int) -> int:
    """
    NumPy approach:
    https://github.com/numpy/numpy/blob/d62b0ee88b20e5946fe49f0ba533b3e547e4d4f1/numpy/core/src/umath/_rational_tests.c.src#L106
    """
    gcd = euclidean_approach(num1, num2)
    num1 //= gcd
    return num1 * num2


if __name__ == "__main__":
    inputs = input()
    a, b = map(int, inputs.split())
    if b > a:
        a, b = b, a
    print(lcm(a, b))
