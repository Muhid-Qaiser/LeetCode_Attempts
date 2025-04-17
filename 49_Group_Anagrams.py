class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if len(strs) == 0:
            return []
            
        groups = []
        hashmap = []

        for i, string in enumerate(strs):
            if groups == []:
                groups.append([strs[i]])
                hashmap.append(self.getHash(string))
            else:
                h = self.getHash(string)
                flag = True
                for idx, dic in enumerate(hashmap[:]):
                    if dic == h:
                        groups[idx].append(string)
                        flag = False
                        break
                if flag:
                    groups.append([string])
                    hashmap.append(h)
        return groups
            


    def getHash(self, str):
        hashmap = defaultdict(int)
        for c in str:
            hashmap[c] = 1 + hashmap.get(c, 0)
        return hashmap

                    
    def isAnagrams(s, t):
        if len(s) != len(t):
            return False
        hash_s, hash_p = defaultdict(str), defaultdict(str)
        for i in range(len(s)):
            if s[i] not in hash_s:
                hash_s[s[i]] = i
            
            if t[i] not in hash_t:
                hash_t[t[i]] = i
            
            if hash_t[t[i]] != hash_s[s[i]]:
                return False
        return True
            
        