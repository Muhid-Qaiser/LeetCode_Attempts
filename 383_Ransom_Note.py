class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        import numpy as np
            
        hashmap = defaultdict(int)
        for c in magazine:
            hashmap[c] = 1 + hashmap.get(c, 0)

        chars, counts = np.unique(list(ransomNote), return_counts=True)

        for char, count in zip(chars, counts):
            if not (char in hashmap and count <= hashmap[char]):
                return False

        return True
        