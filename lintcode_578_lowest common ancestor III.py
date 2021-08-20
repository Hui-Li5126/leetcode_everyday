Description
Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.
The nearest common ancestor of two nodes refers to the nearest common node among all the parent nodes of two nodes (including the two nodes).
Return null if LCA does not exist.

node A or node B may not exist in tree.
Each node has a different value

Example
Example1

Input: 
{4, 3, 7, #, #, 5, 6}
3 5
5 6
6 7 
5 8
Output: 
4
7
7
null
Explanation:
  4
 / \
3   7
   / \
  5   6

LCA(3, 5) = 4
LCA(5, 6) = 7
LCA(6, 7) = 7
LCA(5, 8) = null
Example2

Input:
{1}
1 1
Output: 
1
Explanation:
The tree is just a node, whose value is 1.





>>> class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        # null case
        if not root or not A or not B:
            return None

        # parameter indicates if A/B is in tree
        self.foundA = False
        self.foundB = False

        # find LCA
        lca = self.findLCA(root, A, B)

        # check if A and B in tree
        if self.foundA and self.foundB:
            return lca
        return None

    # helper function to find LCA, return None/A/B
    def findLCA(self, node, A, B):
        # null case
        if not node:
            return None

        # get left/right subtree's LCA
        left_lca = self.findLCA(node.left, A, B)
        right_lca = self.findLCA(node.right, A, B)

        # if node is A/B, found A/B
        if node is A:
            self.foundA = True
        if node is B:
            self.foundB = True

        # check if node is A or B or left/right LCA is not None 
        if node in (A,B) or (left_lca and right_lca):
            return node
        return left_lca or right_lca or None