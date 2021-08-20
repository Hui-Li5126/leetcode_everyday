Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
        
        return output