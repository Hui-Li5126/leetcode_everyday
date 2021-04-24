Given you two strings which are only contain digit character. You need to return a string spliced by the sum of the bits.


>>> class Solution:
    """
    @param A: a string
    @param B: a string
    @return: return the sum of two strings
    """
    def SumofTwoStrings(self, A, B):
        L= []
        p1 = len(A) - 1
        p2 = len(B) - 1
        while p1 >= 0 or p2 >= 0:
            x = ord(A[p1]) - ord("0") if p1 >= 0 else 0
            y = ord(B[p2]) - ord("0") if p2 >= 0 else 0
            value = str(x + y)
            L.append(value)
            p1 -= 1
            p2 -= 1

        return ''.join(i for i in L[::-1])

#similar to leetcode 415 add strings