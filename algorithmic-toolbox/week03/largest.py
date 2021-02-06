from typing import List


def find_largest_number(numbers: List[int], prev=[]) -> int:
    if not len(numbers):
        return sum(num * 10 ** idx for idx, num in enumerate(reversed(prev)))
    else:
        cur_largest_num = max(numbers)
        numbers.remove(cur_largest_num)
        prev.append(cur_largest_num)
        return find_largest_number(numbers, prev)
