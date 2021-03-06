Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        s = set(nodes)
        def dfs(root):
            if not root:
                return root
            if root in s:
                return root
            left, right = dfs(root.left), dfs(root.right)
            if left and right:
                return root
            else:
                return left or right
        return dfs(root)