Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tempStr = ''
        maxLen = 0
        for char in s:
            if char not in tempStr:
                tempStr += char
                maxLen = max(maxLen, len(tempStr))
            else:
                if tempStr[-1] == char:
                    tempStr = '' + char                                       
                else:
                    tempStr ='' + tempStr[tempStr.index(char)+1:] + char
        return maxLen

#TC: O(NM)

#below use hash table, O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=0
        maxlen=0
        h={}
        for i, c in enumerate(s):
            if c in h and start<=h[c]:
                start=h[c]+1
            else:
                maxlen=max(maxlen, i-start+1)
            h[c]=i
        return maxlen