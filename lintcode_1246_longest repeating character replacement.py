Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
    """
    @param s: a string
    @param k: a integer
    @return: return a integer
    """
    def characterReplacement(self, s, k):
        counter = {}
        answer = 0
        j = 0
        # maxFreq 以打擂台的方式记录出现最多的字符数量
        max_freq = 0
        for i in range(len(s)):
            # 当j作为下标合法 且 最少需要被替换的字母数目<=k
            while j < len(s) and j - i - max_freq <= k:
                counter[s[j]] = counter.get(s[j], 0) + 1 
                # 更新出现最多的字符数量
                max_freq = max(max_freq, counter[s[j]])
                j += 1 
            
            # 如果替换 除出现次数最多的字母之外的其他字母 的数目>k,
            # 说明有一个不能换，答案与j-i-1进行比较；
            # 否则说明直到字符串末尾替换数目都<=k，可以全部换掉 
            # 答案与子串长度j-i进行比较
            if j - i - max_freq > k:
                answer = max(answer, j - 1 - i)
            else:
                answer = max(answer, j - i) 
                
            # 起点后移一位，当前起点位置的字母个数-1
            counter[s[i]] -= 1
        return answer

  #TC: O(n)
  #spcace complexity: O(1)