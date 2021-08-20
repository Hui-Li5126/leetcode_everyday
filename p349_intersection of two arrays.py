Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
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
        