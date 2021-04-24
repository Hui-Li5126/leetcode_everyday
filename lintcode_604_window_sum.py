Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        if not nums or len(nums) < k:
            return []
        
        result = []
        j, window_sum = 0, 0
        for i in range(len(nums)):
            while j < len(nums) and j - i < k:
                window_sum += nums[j]
                j += 1
            if j - i == k:
                result.append(window_sum)
            window_sum -= nums[i]

        return result
