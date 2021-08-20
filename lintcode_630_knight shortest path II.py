Description
Given a knight in a chessboard n * m (a binary matrix with 0 as empty and 1 as barrier). the knight initialze position is (0, 0) and 
he wants to reach position (n - 1, m - 1), Knight can only be from left to right. Find the shortest path to the destination position, 
return the length of the route. Return -1 if knight can not reached.

If the knight is at (x, y), he can get to the following positions in one step:

(x + 1, y + 2)
(x - 1, y + 2)
(x + 2, y + 1)
(x - 2, y + 1)
Example
Example 1:

Input:
[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
Output:
3
Explanation:
[0,0]->[2,1]->[0,2]->[2,3]
Example 2:

Input:
[[0,1,0],[0,0,1],[0,0,0]]
Output:
-1



DIRECTIONS = [(-1, -2), (1, -2), (-2, -1), (2, -1),]
class Solution:
    # @param {boolean[][]} grid a chessboard included 0 and 1
    # @return {int} the shortest path
    
    def shortestPath2(self, grid):
        n, m = len(grid), len(grid[0])
        #state: f[i][j]代表从0,0 跳到i, j 的最少步数
        f = [[float('inf')] * m for _ in range(n)]

        # initialize: f[0][0]是起点
        f[0][0] = 0
        
        #function
        for j in range(m): #因为你的i的顺序是不固定的，每一个可能是从上或下转移，但是每一个
        #都是向右走的，所以你的循环是固定顺序的，都是从坐标转移id
            for i in range(n):
                if grid[i][j]:
                    continue
                for delta_x, delta_y in DIRECTIONS:
                    x, y = i + delta_x, j + delta_y
                    if 0 <= x < n and 0 <= y < m:
                        f[i][j] = min(f[i][j], f[x][y] + 1)

        if f[n - 1][m - 1] == float('inf'):
            return -1

        return f[n - 1][m - 1]