Given you two strings which are only contain digit character. You need to return a string spliced by the sum of the bits.
Example
Example1:
Input:
A = "99"
B = "111"
Output: "11010"
Explanation: because 9 + 1 = 10, 9 + 1 = 10, 0 + 1 = 1,connect them，so answer is "11010"
Example2:
Input:
A = "2"
B = "321"
Output: "323"
Explanation: because 2 + 1 = 3, 2 + 0 = 2, 3 + 0 = 3, connect them，so answer is "323"

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