Description
Given k sorted integer arrays, merge them into one sorted array.
Input: 
  [
    [1, 3, 5, 7],
    [2, 4, 6],
    [0, 8, 9, 10, 11]
  ]
Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

>>> import heapq

class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        heap = []
        result = []
        for i, arr in enumerate(arrays):
            if len(arr) > 0:
                heapq.heappush(heap, (arr[0], i, 0))
        
        while len(heap) > 0:
            curr_value, curr_arr_index, curr_index = heapq.heappop(heap)
            curr_arr = arrays[curr_arr_index]
            result.append(curr_value)

            curr_index += 1
            if curr_index < len(curr_arr):
                heapq.heappush(heap, (curr_arr[curr_index], curr_arr_index, curr_index))
        
        return result
#time complexity: O(nlogk) n is number of all elements.
#space complexity: O(K) for heap, 输入的空间是O(N), total O(N+K)