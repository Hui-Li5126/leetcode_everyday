Description
Given an integer array, find a subarray where the sum of numbers is zero. 
Your code should return the index of the first number and the index of the last number.

Example
Example 1:

Input:  [-3, 1, 2, -3, 4]
Output: [0, 2] or [1, 3].
Explanation: return anyone that the sum is 0.
Example 2:

Input:  [-3, 1, -4, 2, -3, 4]
Output: [1,5]	


class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        prefix_hash = {0: -1}
        prefix_sum = 0
        for i, num in enumerate(nums):
            prefix_sum += num
            if prefix_sum in prefix_hash:
                return prefix_hash[prefix_sum] + 1, i 
            prefix_hash[prefix_sum] = i 
        
        return -1, -1