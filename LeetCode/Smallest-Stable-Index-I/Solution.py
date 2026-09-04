1class Solution:
2    def firstStableIndex(self, nums: list[int], k: int) -> int:
3        n = len(nums)
4        suf = [0] * n
5        suf[-1] = nums[-1]
6
7        for i in range(n - 2, -1, -1):
8            suf[i] = min(suf[i + 1], nums[i])
9
10        mx = 0
11        for i, x in enumerate(nums):
12            mx = max(mx, x)
13            if mx - suf[i] <= k:
14                return i
15
16        return -1