Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def exists(root, target):
            if not root:
                return False

            return root == target or exists(root.left, target) or exists(root.right, target)

        def lca(root, p, q):
            if not root:
                return None

            if root == p or root == q:
                return root

            left = lca(root.left, p, q)
            right = lca(root.right, p, q)

            if left and right:
                return root
            elif left:
                return left
            elif right:
                return right

        if not exists(root, p) or not exists(root, q):
            return None

        return lca(root, p, q)