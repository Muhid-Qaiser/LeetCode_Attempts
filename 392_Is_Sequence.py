class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) <= 0:
            return True

        s = list(s)
        for j in range(len(t)):
            if t[j] == s[0]:
                s.pop(0)

                if len(s) <= 0:
                    return True

        return False
        