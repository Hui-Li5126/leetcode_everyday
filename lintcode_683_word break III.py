Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, dict):
        if not s or not dict:
            return 0
            
        #将字符全部转化为小写，并将dict转换成hash_stet存储，降低判断子串存在性的时间复杂度
        n, hs = len(s), set()
        s = s.lower()
        for d in dict:
            hs.add(d.lower())

        #dp[i]表示s[0:i](不含s[i])的拆分方法数    
        dp = [0 for _ in range(n + 1)]
        #dp[0]表示空串的拆分方法数
        dp[0] = 1

        for i in range(n):
            for j in range(i,n):
                #若存在匹配，则进行状态转移
                if s[i:j + 1] in hs:
                    dp[j + 1] += dp[i]
                    
        return dp[n]