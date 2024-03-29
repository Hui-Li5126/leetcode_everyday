Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
    
        n, m = len(matrix), len(matrix[0])
        start, end = 0, n*m -1
        while start + 1 < end:
            mid = (start + end) // 2
            if self.get(matrix, mid) < target:
                start = mid
            else:
                end = mid
    
        if self.get(matrix, start) == target:
            return True
        if self.get(matrix, end) == target:
            return True
        return False

    def get(self, matrix, index):
        x = index // len(matrix[0])
        y = index % len(matrix[0])
        return matrix[x][y]  