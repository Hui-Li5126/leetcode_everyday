Description
Given some points and an origin in two-dimensional space,Find k points from points which are closest to origin Euclidean.Return to the 
answer from small to large according to Euclidean distance. If two points have the same Euclidean distance, they are sorted by x values. 
If the x value is the same, then we sort it by the y value.



>>> """
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""


import heapq

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        # write your code here
        self.heap = []
        for point in points:
            dist = self.get_distance(point, origin)
            heapq.heappush(self.heap, (dist, point.x, point.y))
        
        result = []
        for _ in range(k):
            _, x, y = heapq.heappop(self.heap)
            result.append(Point(x, y))
        
        return result

    def get_distance(self, a, b):
        return (a.x - b.x)**2 + (a.y - b.y)**2

#time complexity: O(n+klogn), for the first foor loop, build heap O(n), second for loop, heappop logn, pop k times, so it's O(klogn)
#when n>>k, it's O(n), better than O(nlogk)