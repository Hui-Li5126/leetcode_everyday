Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sys
class Solution:
    def findSubtree(self, root):
        self.max_sum = -sys.maxsize
        self.ans = root
        self.dfs(root)
        return self.ans
        
    def dfs(self, node):
        if not node:
            return 0
            
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        s = node.val + left + right
        
        if s > self.max_sum:
            self.max_sum = s
            self.ans = node
        
        return s