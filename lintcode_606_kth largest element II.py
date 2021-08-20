Description
Find K-th largest element in an array, and N is much larger than k. Note that it is the kth largest element in the sorted order, not the kth distinct element.

You can swap elements in the array

Example
Example 1:

Input:[9,3,2,4,8],3
Output:4
Example 2:

Input:[1,2,3,4,5,6,8,9,10,7],10
Output:1



>>> from heapq import heapify, heappushpop

class Solution:
    
    def kthLargestElement2(self, nums, k):
        
        min_heap = nums[:k]
        heapify(min_heap)
        
        for num in nums[k:]:
            heappushpop(min_heap, num)
            
        return min_heap[0]
#就用堆的情况下的最优解。

#关键在两个小细节： 1. heapify 一个K项数组先，就不用N次check堆是不是超K了。
# 2. 用heappushpop而不是push再pop，利于堆直接替换再做一次siftdown。

#小细节见功力啊，碰到容易题，你怎么才能出众呢？