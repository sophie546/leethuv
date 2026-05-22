1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        n = len(nums)
4        rot = bisect_left(nums, True, key=lambda n: n <= nums[-1])
5        
6        lo, hi = 0, n - 1
7
8        while lo <= hi:
9            mid = (lo + hi) // 2
10            real = (mid + rot) % n
11
12            if nums[real] == target:
13                return real
14                
15            if nums[real] < target:
16                lo = mid + 1
17            else:
18                hi = mid - 1
19
20        return -1