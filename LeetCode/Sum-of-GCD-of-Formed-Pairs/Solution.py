1class Solution:
2    def gcdSum(self, A: list[int]) -> int:
3        maxi, n = 0, len(A)
4
5        for i in range(n):
6            maxi = max(maxi, A[i])
7            A[i] = gcd(A[i], maxi)
8
9        A.sort()
10
11        return sum(gcd(A[i], A[~i]) for i in range(n // 2))