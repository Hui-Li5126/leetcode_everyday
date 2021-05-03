Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
    """
    @param: : the root of tree
    @param: : the target sum
    @return: two numbers from tree which sum is n
    """

    def twoSum(self, root, n):
        # write your code here
        if not root:
            return
        self.res = None
        node_set = set()
        self.inorder(root, n, node_set)
        return self.res
    
    def inorder(self, root, n, node_set):
        if not root:
            return
        self.inorder(root.left, n, node_set)
        if root.val in node_set:
            self.res = [n - root.val, root.val]
        else:
            node_set.add(n - root.val)
        self.inorder(root.right, n, node_set)