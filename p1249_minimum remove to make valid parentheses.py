Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        Greedy : 1. push in idx stack if '(' 
        if ')': if stack: removeBuffer.append(stack.pop()) else: removeBuffer.append(idx)
        if stack: remove all the '(' as well

        Time : O(2n) => O(n), Space: O(n)
        """
        
        stack = []
        removeBuffer = set()
        
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    removeBuffer.add(i)
        
        while stack:
            removeBuffer.add(stack.pop())

        res = ''
        for i, c in enumerate(s):
            res = res + c if i not in removeBuffer else res
        
        return res