Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
    """
    @param n: An integer
    @return: An Integer
    """
    def climbStairs2(self, n):
        if n <= 1:
            return 1
        if n == 2:
            return 2
        a, b, c = 1, 1, 2
        for i in range(3, n + 1):
            a, b, c = b, c, a + b + c
        return c

#TC: O(n) 对数组进行一次遍历
#space complexity: O(1)
