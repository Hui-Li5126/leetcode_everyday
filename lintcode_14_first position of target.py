Description
Given a sorted array (ascending order) and a target number, find the first index of this number in O(log n)O(logn) time complexity.

If the target number does not exist in the array, return -1.

Example 1:
Input:
tuple = [1,4,4,5,7,7,8,9,9,10]
target = 1

Output:
0

Example 2:
tuple = [1, 2, 3, 3, 4, 5, 10]
target = 3
Output:
2



>>> class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position lefts from 0.
    """
    def binarySearch(self, nums, target):
        # write your code here
        if not nums:
            return -1

        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            elif nums[mid] < target:
                left = mid 
           

        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        return -1