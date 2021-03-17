Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
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
