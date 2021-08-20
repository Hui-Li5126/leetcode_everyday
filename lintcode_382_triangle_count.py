Description
Given an array of integers, how many three numbers can be found in the array, so that we can build an triangle whose three edges 
length is the three numbers that we find?

Example 1:
Input: [3, 4, 6, 7]
Output: 3
Explanation:
They are (3, 4, 6), 
         (3, 6, 7),
         (4, 6, 7)

Example 2:
Input: [4, 4, 4, 4]
Output: 4
Explanation:
Any three numbers can form a triangle. 
So the answer is C(3, 4) = 4





>>>class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        res = 0
        # 先对S进行排序
        S.sort()
        # 最大边从右向左遍历
        for i in range(len(S)-1, 1, -1):
            # 建立双指针
            left = 0
            right = i - 1
            while (left < right):
                # 可以构成三角形
                if S[left] + S[right] > S[i]:
                    res += right - left
                    right -= 1
                # 不能构成三角形
                else:
                    left += 1
        return res

# time complexity: brute force is O(n^3), 这里我们首先固定最大边的位置i, 然后在[0, i-1]之间利用双指针找到满足条件的三边，
#time complexity O(n^2)