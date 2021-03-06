from typing import List

DENOMINATIONS: List[int] = [10, 5, 1]


def get_change(money: int) -> int:
    count = 0
    for denomination in DENOMINATIONS:
        q, money = divmod(money, denomination)
        count += q
    return count


if __name__ == "__main__":
    m = int(input())
    print(get_change(m))
