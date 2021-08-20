Description
A child is running up a staircase with n steps, and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count 
how many possible ways the child can run up the stairs.

For n=0, we think the answer is 1.

Example
Example 1:

Input: 3
Output: 4
Explanation: 1 + 1 + 1 = 2 + 1 = 1 + 2 = 3 = 3 , there are 4 ways.
Example 2:

Input: 4
Output: 7
Explanation: 1 + 1 + 1 + 1 = 1 + 1 + 2 = 1 + 2 + 1 = 2 + 1 + 1 = 





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
