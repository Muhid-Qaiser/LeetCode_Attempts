class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0 :
            return True
        elif len(s) != 0 and len(t) == 0:
            return False

        j = 0
        flag = True

        for i in range(len(t)):
            if s[j] == t[i]:
                flag = True
                j+=1
            elif flag and s[j] == t[i]:
                flag = False

            if j == len(s):
                break

        return j ==  len(s)
        