class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        l, max_val, zc = 0, 0, 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zc += 1
            
            if zc > k:
                if nums[l] == 0:
                    l += 1
                else:
                    while nums[l] == 1:
                        l += 1
                    l += 1
                zc -= 1

            curr = r - l + 1
            if curr > max_val:
                max_val = curr

        return max_val
