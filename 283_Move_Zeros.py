class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = nums.count(0)

        while n:
            idx = nums.index(0)
            nums.pop(idx)
            nums.append(0)
            n -= 1

        return nums
        