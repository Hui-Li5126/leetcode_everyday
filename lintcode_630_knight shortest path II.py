
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