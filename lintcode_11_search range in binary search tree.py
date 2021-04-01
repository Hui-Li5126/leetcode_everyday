Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        # write your code here
        ans = []
        self.travel(root, k1, k2, ans)
        return ans 

    def travel(self, root, k1, k2, ans):
        if root is None:
            return 
        if root.val > k1:
            self.travel(root.left, k1, k2, ans)
        if k1 <= root.val <= k2:
            ans.append(root.val)
        if root.val < k2:
            self.travel(root.right, k1, k2, ans)