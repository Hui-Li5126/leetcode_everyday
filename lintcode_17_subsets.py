Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        n = len(nums)
        nums.sort()
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
        
        return output

# Time complexity: O(N*2^N) to generate all subsets and then copy them into output list.
# Space complexity: O(N*2^N). This is exactly the number of solutions for subsets mulitplied by the number N of elements to keep for each
#subset.  
>>> class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        nums = sorted(nums)
        combinations = []
        self.dfs(nums, 0, [], combinations)
        return combinations
        
    def dfs(self, nums, index, combination, combinations):
        combinations.append(list(combination))
        
        for i in range(index, len(nums)):
            combination.append(nums[i])
            self.dfs(nums, i + 1, combination, combinations)
            combination.pop()
# I think the time complexity is the same as above, space complexity O(N), but not sure.