class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '': return True
        l, r = 0, 0
        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                l += 1
                if l == len(s):
                    return True
            r += 1
        return False
        

        