
Description
Given a sorted array of n integers, find the starting and ending position of a given target value.

If the target is not found in the array, return [-1, -1].

Example
Example 1:

Input:

array = []
target = 9
Output:

[-1,-1]
Explanation:

9 is not in the array.

Example 2:

Input:

array = [5, 7, 7, 8, 8, 10]
target = 8
Output:

[3,4]
Explanation:

The [3,4] subinterval of the array 1 has the value 8.

Challenge
O(log n) time.


>>> class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        if len(A) == 0:
            return [-1, -1]
        
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
            return [-1, -1]
        
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
        return [leftBound, rightBound]
# TC: two O(logn), 
#spcace complexity: O(1)