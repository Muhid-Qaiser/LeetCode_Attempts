class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        curr_val, max_val = sum(nums[:k]), sum(nums[:k])

        for i in range(k, len(nums)):
            curr_val += nums[i] - nums[i-k]

            max_val = max(curr_val, max_val)

        return max_val / k
        