class Solution:
    def processStr(self, s: str, k: int) -> str:
        ln = 0
        
        for c in s:
            if c not in "#*%":
                ln += 1
            elif c == "*" and ln > 0:
                ln -= 1
            elif c == "#":
                ln *= 2

        if k < ln:
            for c in reversed(s):
                if c not in "#*%":
                    ln -= 1
                    if ln == k:
                        return c
                elif c == "*":
                    ln += 1
                elif c == "#":
                    ln //= 2
                    if k >= ln:
                        k -= ln
                else:
                    k = ln - 1 - k

        return '.'