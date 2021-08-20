Description
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct 
friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. 
And you have to output the total number of friend circles among all the students.

1.1≤N≤200. 2.M[i][i] = 1 for all students. 3.If M[i][j] = 1, then M[j][i] = 1.

Example
Example 1:

Input: [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Explanation:
The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.
Example 2:

Input: [[1,1,0],[1,1,1],[0,1,1]]
Output: 1
Explanation:
The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.



>>> 
import collections

class Solution:
    def beginbfs(self, M):
        # 人数
        n = len(M)
        # 答案
        ans = 0
        # 标记是否访问过
        visisted = {}
        for i in range(n):
            visisted[i] = False
        # 遍历每个人，如果这个人还没访问过 就从这个人开始做一遍bfs
        for i in range(n):
            if (visisted[i] == False):
                ans += 1
                q = collections.deque()
                # 标记起点并压入队列
                visisted[i] = True
                q.append(i)
                while (len(q) != 0):
                    # 取出队首
                    now = q.popleft()
                    # 从队首找朋友
                    for j in range(n):
                        # 找到新朋友（之前没访问过的朋友）就标记访问并压入队列
                        if (M[now][j] == 1 and visisted[j] == False):
                            visisted[j] = True
                            q.append(j)
        return ans
    """
    @param M: a matrix
    @return: the total number of friend circles among all the students
    """
    def findCircleNum(self, M):
        # Write your code here
        ansbfs = self.beginbfs(M)
        return ansbfs