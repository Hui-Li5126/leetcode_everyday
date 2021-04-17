Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
    """
    @param str: the string
    @return: the number of substrings 
    """
    def stringCount(self, str):
        if not str:
            return 0
    
        j, answer = 1, 0
        for i in range(len(str)):
            if str[i] != '0':
                continue
            j = max(j, i + 1)
            while  j < len(str) and str[j] == '0':
                j += 1
            answer += j - i
        
        return answer