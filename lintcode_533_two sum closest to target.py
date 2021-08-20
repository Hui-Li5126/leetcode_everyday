Description
Given an array nums of n integers, find two integers in nums such that the
sum is closest to a given number, target.

Return the absolute value of difference between the sum of the two numbers and
the target.

Example 1:
Input:  nums = [-1, 2, 1, -4] and target = 4
Output: 1
Explanation:
The minimum difference is 1. (4 - (2 + 1) = 1).

Example 2:
Input:  nums = [-1, -1, -1, -4] and target = 4
Output: 6
Explanation:
The minimum difference is 6. (4 - (- 1 - 1) = 6).



class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """
    def twoSumClosest(self, nums, target):
        # write your code here
        nums.sort()
        
        ret = float('inf')
        left, right = 0, len(nums)-1
        while left < right:
            this_sum = nums[left] + nums[right]
            ret = min(ret, abs(this_sum-target))
            if this_sum > target:
                right-=1
            else:
                left+=1
        return ret
