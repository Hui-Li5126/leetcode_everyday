Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        if len(numbers) < 3:
            return []
        
        numbers.sort()
        res = []
        
        for i in range(len(numbers)):
            
            left = i + 1
            right = len(numbers)-1
            
            while left < right:
                
                sum_ = numbers[i] + numbers[left] + numbers[right]
                
                if sum_ == 0 and [numbers[i], numbers[left], numbers[right]] not in res:
                    res.append([numbers[i], numbers[left], numbers[right]])
                    
                if sum_ >= 0:
                    right -= 1
                else:
                    left += 1
            
        return res