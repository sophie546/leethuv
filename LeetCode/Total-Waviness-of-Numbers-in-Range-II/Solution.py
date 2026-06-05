1class Solution:
2    waves = []
3    for i in range(1000):
4        r = i % 10
5        m = (i // 10) % 10
6        l = (i // 100) % 10
7        if (m > max(l, r)) | (m < min(l, r)):
8            waves.append(i)
9
10    def totalWaviness(self, A: int, B: int) -> int:
11        return self.waveCount(B) - self.waveCount(A - 1)
12
13    def waveCount(self, num):
14        if num < 100: return 0
15        return sum(self.countWays(num, p) for p in self.waves)
16
17    def countWays(self, num, pattern):
18        s = str(num)
19        n = len(s)
20        t = pattern < 100
21        count = 0
22        for i in range(n - 2):
23            pre = int(s[:i] or 0)
24            cur = int(s[i:i+3])
25            suf = int(s[i+3:] or 0)
26            mult = 10 ** (n - i - 3)
27            ways = 0
28
29            if cur > pattern:
30                ways = pre - t + 1
31            elif cur == pattern:
32                ways = max(0, pre - t)
33                count += suf + 1                
34            else:
35                ways = max(0, pre - t)
36            count += ways * mult
37
38        return count