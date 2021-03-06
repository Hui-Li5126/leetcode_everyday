Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        parents = set()
        curr = p

        while curr:
            parents.add(curr)
            curr = curr.parent


        curr = q

        while curr:
            if curr in parents:
                return curr
            else:
                curr = curr.parent