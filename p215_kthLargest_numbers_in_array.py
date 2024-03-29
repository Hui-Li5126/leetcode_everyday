leetcode 215: Kth largest element in an array
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or k < 1 or k > len(nums):
            return None
        return self.partition(nums, 0, len(nums) - 1, k - 1)
    
    def partition(self, nums, start, end, k):
        if start == end:
            return nums[k]
        
        left, right = start, end
        pivot = nums[(start + end) // 2]
        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
        if k <= right:
            return self.partition(nums, start, right, k)
        if k >= left:
            return self.partition(nums, left, end, k)
        
        return nums[k]



Below is lintcode 461 kth smallest numbers in unsorted array
>>> class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kthSmallest(self, k, nums):
        # write your code here
        if not nums or k < 1 or k > len(nums):
            return None
        return self.partition(nums, 0, len(nums) - 1, k - 1)
        
    def partition(self, nums, start, end, k):
        """
        During the process, it's guaranteed start <= k <= end
        """
        if start == end:
            return nums[k]
            
        left, right = start, end
        pivot = nums[(start + end) // 2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1
                
        # left is now bigger than right
        if k <= right:
            return self.partition(nums, start, right, k)
        if k >= left:
            return self.partition(nums, left, end, k)
        
        return nums[k]



