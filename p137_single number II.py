class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        for k in d.keys():
            if d[k] == 1:
                return k

        
from collections import Counter
class Solution:
    def singleNumber(self, nums):
        hashmap = Counter(nums)
            
        for k in hashmap.keys():
            if hashmap[k] == 1:
                return k

#above hashmap tc: O(N), space complexity: O(N)

#Below 

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # approach: by drawing truth table for 00 -> 01 -> 10 -> 00
        #           l' = ~h & (l ^ i)
        #           h' = ~l' & (h ^ i)
        
        low_bits = high_bits = 0
        for num in nums:
            low_bits = ~high_bits & (low_bits ^ num)
            high_bits = ~low_bits & (high_bits ^ num)
        return low_bits

# https://lenchen.medium.com/leetcode-137-single-number-ii-31af98b0f462