
>>> import heapq

class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        # write your code here
        return heapq.nlargest(k, nums)

>>> 
>>> class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        # write your code here
        self.quick_select(nums, 0, len(nums) - 1, k)
        res =  nums[:k]
        res.sort(reverse=True)
        return res
        
        
    def quick_select(self, nums, start, end, k):
        
        if start == end:
            return
        
        pivot = nums[(start + end) // 2]
        left, right = start, end
        while left <= right:
            while left <= right and nums[left] > pivot:  #左边放大的
                left += 1
            
            while left <= right and nums[right] < pivot:
                right -= 1
            
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
                
        if k <= right:
            self.quick_select(nums, start, right, k)
        if k >= left:
            self.quick_select(nums, left, end, k )