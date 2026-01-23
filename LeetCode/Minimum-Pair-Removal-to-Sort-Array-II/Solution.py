1class Solution:
2    def minimumPairRemoval(self, nums: List[int]) -> int:
3        n = len(nums)
4        if n <= 1:
5            return 0
6
7        arr = [int(x) for x in nums]
8        removed = [False] * n
9        heap = []
10        asc = 0
11        for i in range(1, n):
12            heapq.heappush(heap, (arr[i - 1] + arr[i], i - 1))
13            if arr[i] >= arr[i - 1]:
14                asc += 1
15        if asc == n - 1:
16            return 0
17
18        rem = n
19        prev = [i - 1 for i in range(n)]
20        nxt = [i + 1 for i in range(n)]
21
22        while rem > 1:
23            if not heap:
24                break
25            sumv, left = heapq.heappop(heap)
26            right = nxt[left]
27            if right >= n or removed[left] or removed[right] or arr[left] + arr[right] != sumv:
28                continue
29
30            pre = prev[left]
31            after = nxt[right]
32
33            if arr[left] <= arr[right]:
34                asc -= 1
35            if pre != -1 and arr[pre] <= arr[left]:
36                asc -= 1
37            if after != n and arr[right] <= arr[after]:
38                asc -= 1
39
40            arr[left] += arr[right]
41            removed[right] = True
42            rem -= 1
43
44            if pre != -1:
45                heapq.heappush(heap, (arr[pre] + arr[left], pre))
46                if arr[pre] <= arr[left]:
47                    asc += 1
48            else:
49                prev[left] = -1
50
51            if after != n:
52                prev[after] = left
53                nxt[left] = after
54                heapq.heappush(heap, (arr[left] + arr[after], left))
55                if arr[left] <= arr[after]:
56                    asc += 1
57            else:
58                nxt[left] = n
59
60            if asc == rem - 1:
61                return n - rem
62
63        return n
64