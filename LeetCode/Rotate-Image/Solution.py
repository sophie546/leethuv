1class Solution:
2    def rotate(self, mat: list[list[int]]) -> None:
3        n = len(mat)
4        for i in range(n >> 1):
5            for j in range(i, n - 1 - i):
6                mat[i][j], mat[j][~i], mat[~i][~j], mat[~j][i] = \
7                mat[~j][i], mat[i][j], mat[j][~i], mat[~i][~j]