class Solution:
    def climbStairs(self, n: int) -> int:
#climbStairs use recursive will exceed the time limit
        prev, current =0, 1
        for i in range(n):
            prev, current=current, prev+current
        return current


class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        
        dp = [0]*n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i -2]
            
        return dp[n-1]
    
