Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        numbers.sort()
        ans = None
        for i in range(len(numbers)):
            left, right = i + 1, len(numbers) - 1
            while left < right:
                sum = numbers[left] + numbers[right] + numbers[i]
                if ans is None or abs(sum - target) < abs(ans - target):
                    ans = sum
                    
                if sum <= target:
                    left += 1
                else:
                    right -= 1
        return ans

#时间复杂度:数组排序的时间复杂度为O(nlogn)
#遍历过程，固定值为 n 次，双指针为 n 次，时间复杂度为 O(n2))
#总时间复杂度：O(nlogn)+O(n2)=O(n2)
#空间复杂度为O（1），只需要常量空间。