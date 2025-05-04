class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        nums.sort()
        l, r = 0, len(nums)-1
        count = 0

        while l < r:
            sum_val = nums[l] + nums[r]

            if sum_val > k:
                r -= 1
            elif sum_val < k:
                l += 1
            else:
                l += 1
                r -= 1
                count += 1

        return count
        