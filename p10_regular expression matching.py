Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.is_match_helper(s, 0, p, 0, {})
        
        
    # source 从 i 开始的后缀能否匹配上 pattern 从 j 开始的后缀
    # 能 return True
    def is_match_helper(self, source, i, pattern, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        
        # source is empty
        if len(source) == i:
            return self.is_empty(pattern[j:])
            
        if len(pattern) == j:
            return False
            
        if j + 1 < len(pattern) and pattern[j + 1] == '*':
            matched = self.is_match_char(source[i], pattern[j]) and self.is_match_helper(source, i + 1, pattern, j, memo) or \
                self.is_match_helper(source, i, pattern, j + 2, memo)
        else:                
            matched = self.is_match_char(source[i], pattern[j]) and self.is_match_helper(source, i + 1, pattern, j + 1, memo)
        
        memo[(i, j)] = matched
        return matched
        
        
    def is_match_char(self, s, p):
        return s == p or p == '.'
        
    def is_empty(self, pattern):
        if len(pattern) % 2 == 1:
            return False
        
        for i in range(len(pattern) // 2):
            if pattern[i * 2 + 1] != '*':
                return False
        return True  