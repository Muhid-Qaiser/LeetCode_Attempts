class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        length, max_val = 0, 0
        nums = set(nums)

        for num in nums:
            if num-1 not in nums:
                length = 1
                temp = num + 1
                while temp in nums:
                    length += 1 
                    temp += 1
                if length > max_val:
                    max_val = length
        return max_val
        