class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        min_len = float('inf')
        left, right = 0, 0
        sum_val = 0

        for right in range(len(nums)):
            sum_val += nums[right]

            while sum_val >= target:
                curr_len = right - left + 1
                if min_len > curr_len:
                    min_len = curr_len
                
                sum_val -= nums[left]
                left += 1
        
        if min_len == float('inf'):
            return 0
        return min_len
