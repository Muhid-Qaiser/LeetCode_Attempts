class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res = ""
        max_res = ""
        for c in s:
            res += c

            if res.count(c) > 1:
                res = res[res.index(c)+1:]
            elif len(max_res) < len(res):
                max_res = res
    
        return len(max_res)
        