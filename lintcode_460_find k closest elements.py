


Description
Given target, a non-negative integer k and an integer array A sorted in ascending order, find the k closest numbers to target in A, 
sorted in ascending order by the difference between the number and target. 
Otherwise, sorted in ascending order by number if the difference is same.

Example 1:
Input: A = [1, 2, 3], target = 2, k = 3
Output: [2, 1, 3]

Example 2:

Input: A = [1, 4, 6, 8], target = 3, k = 3
Output: [4, 1, 6]





>>> class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        """
        Binary search to find the closest positions (low and high). [logN]
        Then compare abs(target-A[low]) and ans(target-A[high]), adding the closet element til results reach K-length. [K]
        """
        low, high = 0, len(A) - 1
        while low + 1 < high:
            mid = (low + high) // 2
            if A[mid] < target:
                low = mid
            else:
                high = mid
        
        result = []
        while len(result) != k:
            left_diff = abs(A[low] - target) if low >= 0 else None
            right_diff = abs(A[high] - target) if  high < len(A) else None
            
            # 这里容易出现一个bug是直接写成简写: if right_diff and left_diff
            # 而python 里 0 会被当成false，所以要显示比对
            if right_diff != None and left_diff != None:
                if right_diff < left_diff:
                    result.append(A[high])
                    high += 1
                else:
                    result.append(A[low])
                    low -= 1
            elif right_diff != None:
                result.append(A[high])
                high += 1
            elif left_diff != None:
                result.append(A[low])
                low -= 1
            else:
                break

        return result



#second solution:

class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        """
        Binary search to find the closest positions (low and high). [logN]
        Then compare abs(target-A[low]) and ans(target-A[high]), adding the closet element til results reach K-length. [K]
        """
        right = self.findUpperClosest(A, target)
        left = right - 1

        results = []
        for _ in range(k):
            if self.isLeftCloser(A, target, left, right):
                results.append(A[left])
                left -= 1
            else:
                results.append(A[right])
                right += 1
        return results

    def findUpperClosest(self, A, target):
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] >= target:
                end = mid
            else:
                start = mid

        if A[start] >= target:
            return start 

        if A[end] >= target:
            return end

        return len(A)

    def isLeftCloser(self, A, target, left, right):
        if left < 0:
            return False
        if right >= len(A):
            return True 
        return target - A[left] <= A[right] - target