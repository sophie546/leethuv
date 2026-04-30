class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        @cache
        def dp(r, c, k):
            if grid[r][c] != 0: k -= 1
            if k < 0: return float('-inf')
            if r == rows-1 and c == cols-1: return grid[r][c]
            ans = float('-inf')
            if c + 1 < cols: ans = max(ans, grid[r][c] + dp(r, c + 1, k))
            if r + 1 < rows: ans = max(ans, grid[r][c] + dp(r + 1, c, k))
            return ans
        ans = dp(0, 0, k)
        return ans if ans != float('-inf') else -1