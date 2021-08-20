Merge two given sorted ascending integer array A and B into a new sorted integer array.
Example
Example 1:

Input:

A = [1]
B = [1]
Output:

[1,1]
Explanation:

return array merged.

Example 2:

Input:

A = [1,2,3,4]
B = [2,4,5,6]
Output:

[1,2,2,3,4,4,5,6]


>>> class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        ans = []
        pointA = 0
        pointB = 0
        while pointA < len(A) and pointB <len(B):
            if A[pointA] <= B[pointB]:
                ans.append(A[pointA])
                pointA += 1
            else:
                ans.append(B[pointB])
                pointB += 1
        
        ans = ans + A[pointA:] + B[pointB:]

        return ans