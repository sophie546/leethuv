1class Solution:
2    def minMoves(self, nums: List[int], limit: int) -> int:
3        n = len(nums)
4        delta = [0] * (2 * limit + 2)
5
6        for i in range(n // 2):
7            mini = min(nums[i], nums[-1 - i])
8            maxi = max(nums[i], nums[-1 - i])
9
10            delta[2] += 2
11            delta[mini + 1] -= 1
12            delta[mini + maxi] -= 1
13            delta[mini + maxi + 1] += 1
14            delta[maxi + limit + 1] += 1
15
16        res = n
17        moves = 0
18
19        for targ in range(2, 2 * limit + 1):
20            moves += delta[targ]
21            res = min(res, moves)
22
23        return res
24