class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i, num in enumerate(nums):
            key = target - num
            temp = nums[:i] + nums[i+1:]
            if key in temp:
                return [i, temp.index(key)+1]
        