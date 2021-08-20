Description
Given a string str containing only 0 or 1, please return the number of substrings that consist of 0 .

1<=|str|<=30000

Example
Example 1:

Input:
"00010011"
Output:
9
Explanation:
There are 5 substrings of "0",
There are 3 substrings of "00",
There is 1 substring of "000".
So return 9
Example 2:

Input:
"010010"
Output:
5



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