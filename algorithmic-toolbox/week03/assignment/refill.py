import sys
from numbers import Number
from typing import List


IMPOSSIBLE = -1


def min_refill(stations: List[Number], limit: int):
    """
    Don't forget to add start and end point into stations variable.
    If you need further investigation, check this one:
    https://stackoverflow.com/q/61570575/7093905
    """
    num_refills = current_refill = 0

    while current_refill < len(stations) - 1:
        last_refill = current_refill

        # find the farthest point, if it is possible:
        # first condition: checks to make sure we are reached to the destination
        # second condition: is this the farthest stations?
        while (current_refill < len(stations) - 1) and (
            stations[current_refill + 1] - stations[last_refill] <= limit
        ):
            current_refill += 1

        # we couldn't find neXt step
        if current_refill == last_refill:
            # raise ValueError("Impossible to reach the destination.")
            return IMPOSSIBLE

        if current_refill < len(stations) - 1:
            num_refills += 1

    return num_refills


if __name__ == "__main__":
    # read data
    destination, limit, _, *stations = map(int, sys.stdin.read().split())

    # make it ready for our algorithm
    stations.insert(0, 0)
    stations.append(destination)

    print(min_refill(stations, limit))
