Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
    def validPalindrome(self, s: str) -> bool:
        S_1=list(s)
        S_2=list(s)
        if s==s[::-1]:
            return True
        for i in range(len(s)//2):
            if  s[i]!=s[-1-i]:
                S_1.pop(i)
                S_2.pop(-1-i)
                if S_1==S_1[::-1] or S_2==S_2[::-1]:
                    return True
                else:
                    return False
        return True