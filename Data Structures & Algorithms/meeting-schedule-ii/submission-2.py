"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        pq = []
        intervals.sort(key=lambda x: x.start)
        for interval in intervals:

            if pq and interval.start >= pq[0]:
                heapq.heappop(pq)
            
            heapq.heappush(pq, interval.end)

        return len(pq)
        