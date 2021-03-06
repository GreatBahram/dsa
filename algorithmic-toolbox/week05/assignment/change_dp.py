#!/usr/bin/env python3
"""Money Chang problem Dynamic programming solution:
We are going to solve this exercise in two ways:
    1. Top-down approach, i.e. recursive.
    2. Bottom-up, using tabulation (matrix).

If you find this hard to understand, you can watch this video to get the gist of it:
    https://www.youtube.com/watch?v=Y0ZqKpToTic
Below video will cover both approaches:
    https://www.youtube.com/watch?v=jgiZlGzXMBw
Change money problem in Python, it's not pythonic!:
    https://www.youtube.com/watch?v=m2Elp9ubY3w
"""

import math
from typing import List

DENOMINATIONS: List[int] = [1, 3, 4]
NOT_FOUND = -1


def greedy_money_change(money: int) -> int:
    """
    >>> greedy_money_change(6) # this is not the optimal solution, as we can change it with 2 coins.
    3
    """
    count = 0
    for d in sorted(DENOMINATIONS, reverse=True):
        quotient, money = divmod(money, d)
        count += quotient
    return count


def coin_change(amount):
    """Solve money change problem using top-down approach."""
    memo = {}

    def recursive_coin_change(amount: int, coins_used: int = 0):
        if amount in memo:
            return memo[amount]

        if amount == 0:
            return amount

        min_tmp = []
        for coin in DENOMINATIONS:
            if amount - coin >= 0:
                min_tmp.append(recursive_coin_change(amount - coin, coins_used + 1))
            else:
                min_tmp.append(math.inf)

        min_change = min(min_tmp) + 1
        memo[amount] = min_change
        return min_change

    output = recursive_coin_change(amount, 0)
    return NOT_FOUND if math.isinf(output) else output


def get_change(money: int) -> int:
    """Solve Money change problem using bottom-up approach.
    https://dev.to/stuttskl/making-change-with-dynamic-programming-481p
    >>> get_change(6)  # this is optimal
    2
    """
    if money == 0:
        return money

    cols = money + 1  # 1 for the first 0 column
    memo = [0] + [math.inf] * money

    for coin in DENOMINATIONS:
        # we ignore the zero column, as we need 0 coin to change it!
        for col_idx in range(1, cols):
            # is it possible to change this amount of money with this coin?
            if col_idx >= coin:
                memo[col_idx] = min(memo[col_idx], memo[col_idx - coin] + 1)

    # the minimum change can be found at the end of this memo object
    minimum_change = memo[-1]
    return NOT_FOUND if math.isinf(minimum_change) else minimum_change


if __name__ == "__main__":
    m = int(input())
    print(get_change(m))
