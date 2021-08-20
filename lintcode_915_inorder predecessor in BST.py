Description
Given a binary search tree and a node in it, find the in-order predecessor of that node in the BST.

If the given node has no in-order predecessor in the tree, return null

Example
Example1

Input: root = {2,1,3}, p = 1
Output: null
Example2

Input: root = {2,1}, p = 2
Output: 1


>>> """
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param p: the given node
    @return: the in-order predecessor of the given node in the BST
    """
    def inorderPredecessor(self, root, p):
        # write your code here
        predecessor = None
        
        while root:
            if root.val >= p.val:
                root = root.left
            else:
                predecessor = root
                root = root.right
        
        return predecessor

#BST 里面找 in-order predecessor, 往左走的时候不记， 往右走的时候记，就行了。