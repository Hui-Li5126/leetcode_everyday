Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        if source == None or target == None:
            return -1
        for i in range(len(source)-len(target)+1):
            if target == source[i:len(target)+i]:
                return i
                break
        else:
            return -1

>>> 
>>> def strStr(self, source, target):
        if not target:
            return -1
    
        for i in range(len(source) - len(target) + 1):
            for j in range(len(target)):
                if source[i + j] != target[j]:
                    break  
            else:
                return i  #if break is executed, then else won't be executed
    
        return -1  #O(n^2)