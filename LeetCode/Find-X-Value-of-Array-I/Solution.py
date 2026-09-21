1class Solution:
2    def resultArray(self, A: List[int], k: int) -> List[int]:
3        res = freq = [0] * k
4
5        for n in A:
6            n %= k
7            cur = [0] * k
8            cur[n] = 1
9
10            for x, y in enumerate(freq):
11                cur[x * n % k] += y
12
13            freq = cur
14            for x, y in enumerate(freq):
15                res[x] += y
16
17        return res