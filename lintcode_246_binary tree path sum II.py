Description
Your are given a binary tree in which each node contains a value. Design an algorithm to get all paths which sum to a given value. The path can starts or ends at any node, 
but it must go in a straight line down.

Example
Example 1:

Input:
{1,2,3,4,#,2}
6
Output:
[[2, 4],[1, 3, 2]]
Explanation:
The binary tree is like this:
    1
   / \
  2   3
 /   /
4   2
for target 6, it is obvious 2 + 4 = 6 and 1 + 3 + 2 = 6.
Example 2:

Input:
{1,2,3,4}
10
Output:
[]
Explanation:
The binary tree is like this:
    1
   / \
  2   3
 /   
4   
for target 10, there is no way to reach it.




>>> """
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths
    def binaryTreePathSum2(self, root, target):
        # Write your code here
        result = []
        path = []
        if root is None:
            return result
        self.dfs(root, path, result, 0,  target)
        return result

    def dfs(self, root, path, result, l, target):
        if root is None:
            return
        path.append(root.val)
        tmp = target
        for i in range(l , -1, -1):
            tmp -= path[i]
            if tmp == 0:
                result.append(path[i:])

        self.dfs(root.left, path, result, l + 1, target)
        self.dfs(root.right, path, result, l + 1, target)

        path.pop()