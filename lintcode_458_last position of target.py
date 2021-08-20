Description
Find the last position of a target number in a sorted array. Return -1 if target does not exist.

Example 1:
Input: nums = [1,2,2,4,5,5], target = 2
Output: 2

Example 2:
Input: nums = [1,2,2,4,5,5], target = 6
Output: -1

>>> class Solution:
    """
    @param nums: An integer array sorted in ascrighting order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, A, target):
        if not A or target is None:
            return -1

        left = 0
        right = len(A) - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if A[mid] == target:
                left = mid 
            elif A[mid] < target:
                left = mid 
            elif A[mid] > target:
                right = mid
    
        if A[right] == target:
            return right
        if A[left] == target:
            return left
        return -1