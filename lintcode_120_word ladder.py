Note, this lintcode is a little different from leetcode 127 word ladder, the input is a dict rather than a list

Description
Given two words (start and end), and a dictionary, find the shortest transformation sequence from start to end, output the length of the 
sequence. Transformation rule such that:
Only one letter can be changed at a time
Each intermediate word must exist in the dictionary. (Start and end words do not need to appear in the dictionary )

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the dictionary.
You may assume beginWord and endWord are non-empty and are not the same.
len(dict) <= 5000, len(start) < 5len(dict)<=5000,len(start)<5


Example 1:
start = "a"
end = "c"
dict =["a","b","c"]
output: 2

Example 2:
start ="hit"
end = "cog"
dict =["hot","dot","dog","lot","log"]
output: 5


class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        dict.add(end)
        queue = collections.deque([start])
        distance = {start: 1}
            
        while queue:
            word = queue.popleft()
            if word == end:

                return distance[word]
            
            for next_word in self.get_next_words(word, dict):
                if next_word in distance:
                    continue
                queue.append(next_word)
                distance[next_word] = distance[word] + 1

        return 0
        
    def get_next_words(self, word, dict):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == char:
                    continue
                next_word = left + char + right
                if next_word in dict:
                    words.append(next_word)

        return words