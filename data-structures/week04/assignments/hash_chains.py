from collections import deque
from typing import Any, List


class Query:
    def __init__(self, query):
        self.type = query[0]
        if self.type == "check":
            self.idx = int(query[1])
        else:
            self.string = query[1]


class HashTable:
    multiplier = 263
    prime = 1_000_000_007

    def __init__(self, bucket_count: int):
        self.cardinality = bucket_count
        self.bucket_count = bucket_count
        self.array = [deque() for _ in range(bucket_count)]

    def hash_func(self, string) -> int:
        ans = 0
        for c in reversed(string):
            ans = (ans * self.multiplier + ord(c)) % self.prime
        return ans % self.cardinality

    def add(self, value: str):
        hash_idx = self.hash_func(value)
        # if item already exists, then ignore it.
        for item in self.array[hash_idx]:
            if item == value:
                return None
        self.array[hash_idx].appendleft(value)

    def remove(self, value: str):
        hash_idx = self.hash_func(value)
        self.array[hash_idx] = deque(
            [item for item in self.array[hash_idx] if item != value]
        )

    def __contains__(self, value: str) -> bool:
        # find method
        hash_idx = self.hash_func(value)
        for item in self.array[hash_idx]:
            if item == value:
                return True
        return False

    def check(self, idx: int) -> List[Any]:
        return self.array[idx]


def process_queries(mapping: HashTable, list_of_queries: List[Query]):
    for query in list_of_queries:
        if query.type == "check":
            print(" ".join(mapping.check(query.idx)))
        else:
            if query.type == "find":
                print("yes" if query.string in mapping else "no")
            elif query.type == "add":
                mapping.add(query.string)
            else:
                # del
                mapping.remove(query.string)


if __name__ == "__main__":
    bucket_count = int(input())
    query_nums = int(input())
    mapping = HashTable(bucket_count)

    # read queries
    queries = [Query(input().split()) for _ in range(query_nums)]

    # process queries
    results = process_queries(mapping, queries)
