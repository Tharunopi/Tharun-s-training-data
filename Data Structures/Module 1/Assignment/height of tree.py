from collections import deque

def network_processor(info, packets):
    buffer_size, num_packets = info
    if num_packets == 0:
        return "Nothing to process"

    buffer = deque()
    current_time = 0
    results = []

    for arrival_time, process_time in packets:
        current_time = max(current_time, arrival_time)
        while buffer and buffer[0] <= current_time:
            buffer.popleft()

        if len(buffer) < buffer_size:
            start_time = max(current_time, arrival_time)
            finish_time = start_time + process_time
            buffer.append(finish_time)
            results.append(start_time)
            current_time = start_time
        else:
            results.append(-1)

    return results


a = [1, 3]
x = [[0, 0], [1, 0], [0, 1]]
print(network_processor(a, x))

# For input from user:
# a = list(map(int, input().split()))
# x = [list(map(int, input().split())) for _ in range(a[1])]
# print(network_processor(a, x))