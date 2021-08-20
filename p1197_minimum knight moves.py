Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import collections

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        directions = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)] 
        queue = collections.deque([(0, 0)])
        distance = {(0, 0): 0}
        
        while queue:
            a, b = queue.popleft()
            if (a, b) == (x, y):
                return distance[(a, b)]
            for dx, dy in directions:
                next_x, next_y = a + dx, b + dy
                if (next_x, next_y) in distance:
                    continue
                distance[(next_x, next_y)] = distance[(a, b)] + 1
                queue.append((next_x, next_y))
