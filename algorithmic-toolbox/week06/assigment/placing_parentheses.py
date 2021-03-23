import math
from copy import deepcopy
from typing import Tuple

OPERATORS: Tuple[str] = ("+", "-", "*")


def naive_placing_parentheses(expression: str):
    """
    In this we generate all posibble values
    Time complexity: op!, where op is the number of operations.
    """
    results = []

    for idx, char in enumerate(expression):
        if char in OPERATORS:
            left = naive_placing_parentheses(expression[0:idx])
            right = naive_placing_parentheses(expression[idx + 1 :])

            for n in left:
                for m in right:
                    results.append(eval(f"{n}{char}{m}"))

    # base case
    if len(results) == 0:
        return [expression]

    return results


def calc(a: int, operator, b: int):
    operator_func_map = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
    }
    func = operator_func_map[operator]
    return func(a, b)


def get_maximum_value(expression: str):
    """
    https://codeblogs.me/algorithms_puzzles/dynamic-programming/arithmetic-expression/arithmetic-expression.html
    """
    digits = []
    operators = []

    for char in expression:
        if char.isdigit():
            digits.append(int(char))
        else:
            operators.append(char)

    memo = [[0 for i in range(len(digits))] for j in range(len(digits))]
    m = deepcopy(memo)
    M = deepcopy(memo)

    for i in range(len(digits)):
        m[i][i] = digits[i]
        M[i][i] = digits[i]

    for s in range(1, len(digits)):
        for i in range(0, len(digits) - s):
            j = i + s
            m[i][j], M[i][j] = min_and_max(m, M, i, j, operators)
    return M[0][-1]


def min_and_max(m, M, i, j, operators):
    min_value = math.inf
    max_value = -math.inf

    for k in range(i, j):
        a = calc(M[i][k], operators[k], M[k + 1][j])
        b = calc(M[i][k], operators[k], m[k + 1][j])
        c = calc(m[i][k], operators[k], M[k + 1][j])
        d = calc(m[i][k], operators[k], m[k + 1][j])

        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)

    return min_value, max_value


if __name__ == "__main__":
    print(get_maximum_value(input()))
