Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if nums is None or not nums:
            return 0
            
        # state: dp[i] 表示以第 i 个数结尾的 LIS 的长度
        # initialization: dp[0..n-1] = 1
        dp = [1] * len(nums)
        
        # function: dp[i] = max(dp[j] + 1), j < i && nums[j] < nums[i]
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # answer, 任意一个位置都可能是 LIS 的结尾  
        return max(dp)