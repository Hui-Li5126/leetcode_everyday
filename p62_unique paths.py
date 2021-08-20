Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # state: dp[i][j] 代表从0，0走到i, j 的总方案数
        dp = [[0] * n for _ in range(m)]
        #dp = [[0] * n] * m 是不对的
        #initialize: 初始化第0行和第0列
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        #function: dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[m - 1][n - 1]