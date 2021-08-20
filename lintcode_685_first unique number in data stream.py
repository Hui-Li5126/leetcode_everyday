Description
Given a continuous stream of data, write a function that returns the first unique number (including the last number) when the 
terminating number arrives. If the terminating number is not found, return -1.

Example 1
Input: 
[1, 2, 2, 1, 3, 4, 4, 5, 6]
5
Output: 3

Example 2:
Input: 
[1, 2, 2, 1, 3, 4, 4, 5, 6]
7
Output: -1

Example 3:
Input: 
[1, 2, 2, 1, 3, 4]
3
Output: 3


>>> class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def firstUniqueNumber(self, nums, number):
        # Write your code here
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            if num == number:
                break
        else:
            return -1
#for if break, else, 如果出现break 就不会进入else
  

        for num in nums:
            if counter[num] == 1:
                return num
            if num == number:
                break
        
        return -1