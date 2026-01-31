1class Solution:
2    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
3        res = letters[0]
4        flag = False
5
6        for ch in letters:
7            if not flag:
8                if ch > target:
9                    res = ch
10                    flag = not flag
11            else:
12                if ch > target and ch < res:
13                    res = ch
14
15        return res