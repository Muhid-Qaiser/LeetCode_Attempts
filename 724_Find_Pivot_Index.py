class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        sum_val = sum(nums)
        left = 0

        for idx, pivot in enumerate(nums):
            if sum_val - left - pivot == left:
                return idx
            left += pivot
        
        return -1


        