1class Solution:
2    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
3        m, n = len(matrix), len(matrix[0])
4        maxArea = 0
5        h = [0] * n
6
7        for i in range(m):
8            for j in range(n):
9                if matrix[i][j] == 1:
10                    h[j] += 1
11                else:
12                    h[j] = 0
13            sh = sorted(h, reverse=True)
14            for j in range(n):
15                if sh[j] == 0:
16                    break
17                maxArea = max(maxArea, sh[j] * (j + 1))
18
19        return maxArea