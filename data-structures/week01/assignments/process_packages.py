"""
https://codereview.stackexchange.com/questions/200950/packet-process-time-simulation-using-queue
"""
from collections import deque, namedtuple

Request = namedtuple("Request", ["arrive_time", "process_time"])


def process_requests(requests, buffer_size: int):
    buffer = deque(maxlen=buffer_size)

    start_times = [None] * len(requests)

    for idx, (arrival, duration) in enumerate(requests):
        # if there is an item inside buffer which is finished, remove it
        while buffer and buffer[0] <= arrival:
            buffer.popleft()

        if len(buffer) >= buffer_size:
            start_times[idx] = -1
        else:
            start_times[idx] = max(arrival, buffer[-1] if buffer else 0)
            buffer.append(start_times[idx] + duration)

    return start_times


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []

    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    responses = process_requests(requests, buffer_size)

    for response in responses:
        print(response)


if __name__ == "__main__":
    main()
