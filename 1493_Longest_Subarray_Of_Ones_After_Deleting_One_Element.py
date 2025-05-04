class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        l, zc, max_val = 0, 0, 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zc += 1

            while zc > 1:
                if nums[l] == 0:
                    zc -= 1
                l += 1
            
            max_val = max(max_val, r-l)
        
        return max_val
        