1class Solution:
2    def minimumDeletions(self, s: str) -> int:
3        res = 0
4        b = 0
5
6        for c in s:
7            if c == 'b':
8                b += 1
9            elif b:
10                res += 1
11                b -= 1
12
13        return res
14