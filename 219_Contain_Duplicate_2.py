class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        hashmap = {}

        for idx, num in enumerate(nums):
            if num in hashmap and abs(hashmap[num] - idx) <= k:
                return True
            else:
                hashmap[num] = idx
        return False



        