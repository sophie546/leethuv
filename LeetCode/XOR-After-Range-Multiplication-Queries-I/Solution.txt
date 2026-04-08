1class Solution:
2    def xorAfterQueries(self, nums, queries):
3        mod = 1000000007
4
5        for t in queries:
6            l = t[0]
7            r = t[1]
8            k = t[2]
9            v = t[3]
10
11            idx = l
12
13            while idx <= r:
14                temp = nums[idx]
15                nums[idx] = (temp * v) % mod
16                idx += k
17
18        ans = 0
19        for num in nums:
20            ans ^= num
21
22        return ans