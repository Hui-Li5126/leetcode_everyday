Description
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
You must do this in-place without making a copy of the array.
Minimize the total number of operations.


>>> class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        left = 0
        index = 0
        while index < len(nums):
            if nums[index] == 0:
                index += 1
            else:
                if left != index:
                    nums[left] = nums[index]
                left += 1
                index += 1

        for i in range(left, len(nums)):
            nums[i] = 0