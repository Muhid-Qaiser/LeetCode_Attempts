class Solution:
    def largestAltitude(self, gain: List[int]) -> int:        
        curr, max_val = 0, 0
        for i in range(len(gain)):
            curr += gain[i]
            max_val = max(curr, max_val)
        return max_val
