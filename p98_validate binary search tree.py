Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValid(root, -sys.maxsize, sys.maxsize)
    
    def isValid(self, node, left, right):
        if not node:
            return True
        if node.val > left and node.val < right:
            return self.isValid(node.left, left, node.val) and self.isValid(node.right, node.val, right)
        else:
            return False
        