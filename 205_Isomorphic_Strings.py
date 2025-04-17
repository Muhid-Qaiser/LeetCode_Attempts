class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        from collections import defaultdict
        hashmap = defaultdict(str)
        res = ""
        
        for i, c in enumerate(s):
            if c not in hashmap:
                hashmap[c] = t[i]

        hashmap = defaultdict(str, { v:k for k,v in hashmap.items() })

        for i, c in enumerate(t):
            res += hashmap[c]
        
        return list(res) == list(s)
            
        