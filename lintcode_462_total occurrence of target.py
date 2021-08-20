
Description
Given a target number and an integer array sorted in ascending order. Find the total number of occurrences of target in the array.

Example
Example1:

Input: [1, 3, 3, 4, 5] and target = 3, 
Output: 2.
Example2:

Input: [2, 2, 3, 4, 6] and target = 4, 
Output: 1.
Example3:

Input: [1, 2, 3, 4, 5] and target = 6, 
Output: 0.
Challenge
Time complexity in O(logn)




>>> class Solution:
    """
    @param A: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def totalOccurrence(self, A, target):
        if len(A) == 0:
            return 0

        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid

        if A[start] == target:
            leftBound = start 
        elif A[end] == target:
            leftBound = end
        else:
            return 0

        start, end = leftBound, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] <= target:
                start = mid
            else:
                end = mid
        if A[end] == target:
            rightBound = end
        else:
            rightBound = start

        return rightBound - leftBound + 1