Description
Return the number of nodes in the kth layer(The layer number starts from 1 and the root node is layer 1).
Example
Example1

Input: root = {3,9,20,#,#,15,7}, k = 2
Output: 2
Explanation:
  3
 / \
9  20
  /  \
 15   7
Example2

Input: root = {3,1,2}, k = 1
Output: 1
Explanation:
  3
 / \
1   2



Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root node
    @param k: an integer
    @return: the number of nodes in the k-th layer of the binary tree
    """
    def kthfloorNode(self, root, k):
        
        if root == None:
            return 0

        q = [root]
        level = 1
        while q:
            size = len(q)
            if level == k:
                return size
            new_q = []
            for node in q:
                if node.left != None:
                    new_q.append(node.left)
                if node.right != None:
                    new_q.append(node.right)
            q = new_q
            level += 1

        return 0