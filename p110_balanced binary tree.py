Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root: TreeNode) -> int:
        if not root:
            return -1
        return 1 + max(self.height(root.left), self.height(root.right))
    
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
       
        return abs(self.height(root.left) - self.height(root.right)) < 2 \
              and self.isBalanced(root.left) \
              and self.isBalanced(root.right)
 




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        is_balanced, _ = self.divideConquer(root)
        return is_balanced
    #定义，判断root 为根的二叉树是否是平衡树并且返回高度是多少
    def divideConquer(self, root):
        #出口： 如果是空树，直接返回是平衡的，高度为0
        if not root:
            return True, 0
        
        #拆解： 拆解到左右子树，得到左右子树是否平衡和高度的信息
        is_left_balanced, left_height = self.divideConquer(root.left)
        is_right_balanced, right_height = self.divideConquer(root.right)
        root_height = max(left_height, right_height) + 1
        
        if not is_left_balanced or not is_right_balanced:
            return False, root_height
        if abs(left_height - right_height) > 1:
            return False, root_height
        return True, root_height           