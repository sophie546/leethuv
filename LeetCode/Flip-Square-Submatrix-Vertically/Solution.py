1class Solution:
2    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
3        for i in range(k):
4            for j in range(k // 2):
5                grid[x + j][y + i], grid[x + k - j - 1][y + i] = grid[x + k - j - 1][y + i], grid[x + j][y + i]
6        return grid
7
8        
9