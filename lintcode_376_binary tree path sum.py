Description
Given a binary tree, find all paths that sum of the nodes in the path equals to a given number target.

A valid path is from root node to any of the leaf nodes.

Example
Example 1:

Input:
{1,2,4,2,3}
5
Output: [[1, 2, 2],[1, 4]]
Explanation:
The tree is look like this:
	     1
	    / \
	   2   4
	  / \
	 2   3
For sum = 5 , it is obviously 1 + 2 + 2 = 1 + 4 = 5
Example 2:

Input:
{1,2,4,2,3}
3
Output: []
Explanation:
The tree is look like this:
	     1
	    / \
	   2   4
	  / \
	 2   3
Notice we need to find all paths from root node to leaf nodes.
1 + 2 + 2 = 5, 1 + 2 + 3 = 6, 1 + 4 = 5 
There is no one satisfying it.






>>> class Solution:
    # @param {TreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths
    def binaryTreePathSum(self, root, target):
        # Write your code here
        result = []
        path = []
        self.dfs(root, path, result, 0,  target)

        return result

    def dfs(self, root, path, result, len, target):
        if root is None:
            return
        path.append(root.val)
        len += root.val

        if root.left is None and root.right is None and len == target:
            result.append(path[:])

        self.dfs(root.left, path, result, len, target)
        self.dfs(root.right, path, result, len, target)

        path.pop()