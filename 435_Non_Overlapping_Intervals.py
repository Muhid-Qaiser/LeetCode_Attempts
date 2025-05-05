class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x : x[1])
        prev, res = float('-inf'), 0

        for i in intervals:
            if prev > i[0]:
                res += 1
            else:
                prev =  i[1]
        
        return res