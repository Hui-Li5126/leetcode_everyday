Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
         # idea: binary search + hash set
        result = set()
        if len(nums1) > len(nums2):
            s_nums = nums2
            b_nums = nums1
        else:
            s_nums = nums1
            b_nums = nums2

        s_nums.sort()
        for num in b_nums:
            if self.binary_seach(s_nums, num):
                result.add(num)
        return list(result)


    def binary_seach(self, nums, target):
        if not nums or len(nums) == 0:
            return False

        start, end = 0, len(nums) -1
        while start + 1 < end:
            middle = start + (end - start) // 2

            if nums[middle] <= target:
                start = middle
            elif nums[middle] > target:
                end = middle

        if nums[end] == target or nums[start] == target:
            return True
        return False

#above is sort smaller array first, then for every element of bigger array, search in smaller array using binary 
#search, if found then add it to set. 
#TC: mlog(m) for sort, then nlog(m) for loop and search, here assume n is bigger than m, total nlog(m)


#below is two pointers, nlogn

class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        # idea: two pointers 
        nums1.sort()
        nums2.sort()
        result = []

        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
                while i < len(nums1) and nums1[i] == nums1[i - 1]:
                    i += 1
                while j < len(nums2) and nums2[j] == nums2[j - 1]:
                    j += 1
                    
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1

        return result