def naive_approach(num1: int, num2: int) -> int:
    if num1 == num2:
        return num1

    gcd = None
    for divisor in range(1, min(num1, num2) + 1):
        if num1 % divisor == 0 and num2 % divisor == 0:
            gcd = divisor
    return gcd


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
