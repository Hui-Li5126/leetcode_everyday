Description
Give a dictionary of words and a sentence with all whitespace removed, return the number of sentences you can form by 
inserting whitespaces to the sentence so that each word can be found in the dictionary.

Ignore case

Example
Example1

Input:
"CatMat"
["Cat", "Mat", "Ca", "tM", "at", "C", "Dog", "og", "Do"]
Output: 3
Explanation:
we can form 3 sentences, as follows:
"CatMat" = "Cat" + "Mat"
"CatMat" = "Ca" + "tM" + "at"
"CatMat" = "C" + "at" + "Mat"
Example1

Input:
"a"
[]
Output: 
0





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