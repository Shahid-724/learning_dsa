def getNumberOfDroppedPackets(requests, max_packets, rate):
    requests.sort()

    current_time = 0
    pipeline = 0
    dropped_packets = 0

    for request in requests:
        request_time, packets = request

        if request_time > current_time:
            elapsed_time = request_time - current_time
            deliverable = elapsed_time * rate
            pipeline = max(0, pipeline - deliverable)
            current_time = request_time

        pipeline += packets

        if pipeline > max_packets:
            dropped_packets += (pipeline - max_packets)
            pipeline = max_packets

    return dropped_packets

# Example usage
requests = [[1, 88058], [22, 23848], [101, 76825], [73, 19339], [45, 59342]]
max_packets = 163
rate = 52
print(getNumberOfDroppedPackets(requests, max_packets, rate))
