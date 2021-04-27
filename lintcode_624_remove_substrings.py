Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
    """
    @param: s: a string
    @param: dict: a set of n substrings
    @return: the minimum length
    """
    def minLength(self, s, dict):
        visited = {}
        queue = collections.deque()
        queue.append(s)
        # 初始化为极大值
        ans = sys.maxsize
        while len(queue) > 0:
            s = queue.popleft()
            for word in dict:
                pos = s.find(word)
                while pos != -1:
                    if s == word:
                        ans = 0
                        break
                    # tvisited为删除下标pos开始的word之后的字符串
                    tvisited = s[:pos] + s[pos + len(word):]
                    # 如果这个字符串没有出现过，压入队列，更新答案
                    if tvisited not in visited:
                        visited[tvisited] = 1
                        # 更新剩下的字符串的最短长度
                        ans = min(ans, len(tvisited))
                        queue.append(tvisited)
                    # 寻找s中下标从pos+1开始到末尾第一次出现的word的首下标
                    pos = s.find(word, pos + 1)
            if ans == 0:
                break
        return ans
#假设有n个单词，原字符串长度为m。因为长度为m的字符串，如果串中字符各不相同，则子串的个数为m(m+1)/2+1，
#因此最坏情况下字符串的子串是O(m^2)级别的,空间复杂度为O(m^2)；

#最坏情况队列中的字符串个数会是O(m^2)级别的，对于每一个字符串都要对n个单词进行查找处理，查找处理的时间复杂度是此时队列中
#头元素的长度ln，最坏取个平均值m/2，因此时间复杂度为O(m^3n).