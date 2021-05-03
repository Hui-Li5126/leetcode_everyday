Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.quick_select(points, 0, len(points) - 1, k)
        res = points[:k]
        return res
    
    def quick_select(self, nums, start, end, k):
        if start == end:
            return
        
        pivot = nums[(start + end) // 2]
        left, right = start, end
        while left <= right:
            while left <= right and (nums[left][0])**2 + (nums[left][1])**2 < (pivot[0])**2 +(pivot[1])**2: 
                left += 1
            
            while left <= right and (nums[right][0])**2 + (nums[right][1])**2 > (pivot[0])**2 +(pivot[1])**2: 
                right -= 1
            
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
                
        if k <= right:
            self.quick_select(nums, start, right, k)
        if k >= left:
            self.quick_select(nums, left, end, k )