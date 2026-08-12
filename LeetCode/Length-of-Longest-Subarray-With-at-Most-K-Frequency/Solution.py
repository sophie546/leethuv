1class Solution:
2    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
3        n, cnt=len(nums), 0
4        freq=defaultdict(int)
5        l=0
6        for r, x in enumerate(nums):
7            freq[x]+=1
8            while freq[x]>k:
9                freq[nums[l]]-=1
10                l+=1
11            cnt=max(cnt, r-l+1)
12        return cnt