from collections import namedtuple
from heapq import heapify, heappop, heappush
from typing import NamedTuple


class AssignedJob(NamedTuple):
    worker: int
    started_at: int


class WorkerMinHeap:
    """
    MinHeap that holds both worker_id and next_free_time for each worker.
    When it comes to pick up, it will return the worker which has the lowest next_free_time.
    """

    def __init__(self, n_workers: int) -> None:
        self.heap = [(0, idx) for idx in range(n_workers)]
        heapify(self.heap)

    def push(self, next_free_time, worker_id):
        heappush(self.heap, (next_free_time, worker_id))

    def pop(self):
        return heappop(self.heap)

    def peek(self):
        return self.heap[0]

    def __len__(self):
        return len(self.heap)


def assign_jobs(n_workers, jobs):
    """
    The problem with this code is that finding the next_free_worker is hard
    we have to iterate over next_free_time array.

    It was a MinHeap data structure then finding it was much more pleasant.
    """
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result


def effective_assign_jobs(n_workers, jobs):
    result = []
    wmh = WorkerMinHeap(n_workers)
    for job in jobs:
        next_free_time, worker_id = wmh.pop()
        result.append(AssignedJob(worker_id, next_free_time))
        wmh.push(next_free_time + job, worker_id)
        # next_free_time[next_worker] += job

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    for job in effective_assign_jobs(n_workers, jobs):
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
