Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:

    """

    @param s: a string which consists of lowercase or uppercase letters

    @return: the length of the longest palindromes that can be built

    """

    def longestPalindrome(self, s):

        #cnt统计字符串s中每种字母出现次数的计数数组

        #OddCount为是否有奇数次字符，1表示有，0表示无

        #ans为最终答案

        ans = 0

        cnt = collections.Counter(s)

        #每种字符可使用cnt/2*2次

        #如果遇到出现奇数次的字符并且中心位置空着，那么答案加1

        for i in cnt.values():

            ans += i // 2 * 2

            if ans % 2 == 0 and i % 2 == 1:

                ans += 1

        return ans

>>> 
>>> class Solution:
    # @param {string} s a string which consists of lowercase or uppercase letters
    # @return {int} the length of the longest palindromes that can be built
    
    # the answer is the count of characters that has even number of appereances.
    # for characters that has odd number of appereances,
    # their appereances minus 1 will make their apperances even.
    # And finally we can put an unused character in the middle of the palindrome
    def longestPalindrome(self, s):
        # Write your code here
        hash = {}

        for c in s:
            if c in hash:
                del hash[c]
            else:
                hash[c] = True

        remove = len(hash)
        if remove > 0:
            remove -= 1
    
        return len(s) - remove

# tc: O(N), space complexity: O(N)