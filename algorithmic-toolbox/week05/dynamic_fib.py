from typing import Dict

memo: Dict[int, int] = {0: 0, 1: 1}

def f(n: int) -> int:
    """
    Solving Fibonacci sequence.
    Bottom-up DAG
    """
    for k in range(1, n+ 1):
        if k <= 2:
            output = k
        elif n not in memo:
            output = memo[k - 1] + memo[k - 2]
        memo[k] = output
    return memo[n]
