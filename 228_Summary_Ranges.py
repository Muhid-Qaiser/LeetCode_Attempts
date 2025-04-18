class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        merged = []

        for i, num in enumerate(nums):
            if merged and num == merged[-1][-1] + 1:
                merged[-1][-1] = num
            else:
                merged.append( [num, num] )

        for idx, interval in enumerate(merged[:]):
            interval = sorted(list(set(interval)))
            if len(interval) > 1:
                merged[idx] = f"{interval[0]}->{interval[1]}"
            else:
                merged[idx] = f"{interval[0]}"

        return merged
        