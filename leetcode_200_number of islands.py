Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    self.bfs(grid, i, j)
        return count
    
    def bfs(self, grid, i, j):
        queue = deque([(i, j)])
        grid[i][j] = '@'
        
        while queue:
            i, j = queue.popleft()
            for delta_i, delta_j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                next_i = i + delta_i
                next_j = j + delta_j
                if next_i < 0 or next_j < 0 or next_i >= len(grid) or next_j >= len(grid[0]) or grid[next_i][next_j] != '1':
                    continue
                queue.append((next_i, next_j))
                grid[next_i][next_j] = '@'
# time complexity: O(MN), worst case 需要travesal 每一条边，小于4MN， space complexity O(min(M,N))

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j)
        return count
    
    def dfs(self, grid, i, j):
	if next_i < 0 or next_j < 0 or next_i >= len(grid) or next_j >= len(grid[0]) or grid[next_i][next_j] != '1':
		return
	grid[i][j] = '@'
        self.dfs(grid, i + 1, j)
	self.dfs(grid, i - 1, j)
	self.dfs(grid, i, j + 1)
	self.dfs(grid, i, j - 1)

#time complexity: O(MN) < 4MN, #space complexity: O(MN), the worst case is snake-wise maze, recursive depth is big, at risk of stack overflow
