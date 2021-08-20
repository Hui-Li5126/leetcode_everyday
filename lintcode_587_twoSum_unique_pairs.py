Description
Given an array of integers, find how many unique pairs in the array such that their sum is equal to a specific target number. 
Please return the number of pairs.

Example 1:
Input: nums = [1,1,2,45,46,46], target = 47 
Output: 2
Explanation:

1 + 46 = 47
2 + 45 = 47

Example 2:

Input: nums = [1,1], target = 2 
Output: 1
Explanation:
1 + 1 = 2






>>> class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here
        nums.sort()
        left = 0
        right =len(nums) - 1
        d = {}
        while left < right:
            if nums[left] + nums[right] == target:
                if nums[left] not in d:
                    d[nums[left]] = True 
                left += 1
                right -= 1 
            elif nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
        
        return len(d)
