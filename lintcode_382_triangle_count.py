Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
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