Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, A):
        left, index, right = 0, 0, len(A) - 1
        # be careful, index < right is not correct
        while index <= right:
            if A[index] == 0:
                A[left], A[index] = A[index], A[left]
                left += 1
                index += 1 # move to next number
            elif A[index] == 2:
                A[right], A[index] = A[index], A[right]
                right -= 1
            else:  # == 1, skip
                index += 1