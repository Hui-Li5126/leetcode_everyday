Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
    def climbStairs(self, n: int) -> int:
#climbStairs use recursive will exceed the time limit
        prev, current =0, 1
        for i in range(n):
            prev, current=current, prev+current
        return current