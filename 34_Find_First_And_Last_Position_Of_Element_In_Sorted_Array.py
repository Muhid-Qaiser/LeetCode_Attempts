class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left = self.binary_search(nums, target, True)
        right = self.binary_search(nums, target, False)

        return [left, right]


    def binary_search(self, nums, target, search_left):

        left = 0
        right = len(nums)-1
        idx = -1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                idx = middle
                if search_left:
                    right = middle - 1
                else:
                    left = middle + 1

        return idx
        