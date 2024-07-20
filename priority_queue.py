# Priority Queue
# https://en.wikipedia.org/wiki/Priority_queue
# Input: intervals = [[0, 30], [5, 10], [15, 20]]
# Output: 2

from heapq import heappush, heappop


def min_meeting_rooms(intervals: list[list[int]]) -> int:
    heap = []
    intervals.sort()

    heappush(heap, intervals[0][1])

    for interval in intervals[1:]:
        if interval[0] >= heap[0]:
            heappop(heap)

        heappush(heap, interval[1])

    return len(heap)
