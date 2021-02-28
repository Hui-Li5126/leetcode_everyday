Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        lib = {word:idx for idx, word in enumerate(words)}
    
        res = []        
        for idx, word in enumerate(words):  
            l = len(word)
            for i in range(l+1):
                pre, post = word[:i], word[i:] 
                if pre == pre [::-1]:
                    if post[::-1] in lib and post[::-1] != word: 
                        res.append([lib[post[::-1]], idx])
                if post == post[::-1] and i != l:
                    if pre[::-1] in lib and pre[::-1] != word: 
                        res.append([idx, lib[pre[::-1]]])
                    
        return res
