Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from heapq import *

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        heap = [intervals[0][1]]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] >= heap[0]:
                heappop(heap)
            
            heappush(heap, intervals[i][1])
            
        return len(heap)