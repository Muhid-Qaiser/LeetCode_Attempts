class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        s_l = s.split()

        if len(s_l) != len(pattern):
            return False

        hash_p, hash_s = defaultdict(str), defaultdict(str)

        for i in range(len(pattern)):
            if pattern[i] not in hash_p:
                hash_p[ pattern[i] ] = i
                
            if s_l[i] not in hash_s:
                hash_s[ s_l[i] ] = i
            
            if hash_p[ pattern[i] ] != hash_s[ s_l[i] ]:
                return False

        return True
        