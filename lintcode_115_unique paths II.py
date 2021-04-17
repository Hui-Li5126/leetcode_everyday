Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        #state dp[i][j]表示从0,0走到i, j 的路径数
        dp = [[0] * m for _ in range(n)]
        #initialize
        for i in range(n):
            if obstacleGrid[i][0]:
                break
            dp[i][0] = 1
        for j in range(m):
            if obstacleGrid[0][j]:
                break
            dp[0][j] = 1

        #function
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j]:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[n - 1][m - 1]