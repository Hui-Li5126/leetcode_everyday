
Description
Given an array of integers, find how many pairs in the array such 
that their sum is bigger than a specific target number. Please return the number of pairs.

>>> class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """
    def twoSum2(self, nums, target):
        # write your code here
        count = 0
        nums.sort()
        left, right = 0, len(nums) -1
        while left < right:
            if nums[left] + nums[right] > target:
                count += right - left
                right -= 1
            else:
                left += 1
        return count

#time complexity, o(nlogn) for sort, 