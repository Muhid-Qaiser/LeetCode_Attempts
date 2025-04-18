class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        merged = []
        for i, interval in enumerate(intervals):
            if merged and merged[-1][-1] >= interval[0]:
                merged[-1][-1] = max( merged[-1][-1], interval[1] )
            else:
                merged.append( interval )
        return merged
        