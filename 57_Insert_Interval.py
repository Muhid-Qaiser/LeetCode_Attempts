class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if intervals == []:
            return [ newInterval ]
        for idx, interval in enumerate(intervals):
            if interval[1] >= newInterval[0] and interval[0] <= newInterval[0]:
                interval[1] = max(newInterval[1], interval[1])

                if idx < len(intervals)-1:
                    prev = None
                    for i, next_inter in enumerate(intervals[idx+1:]):
                        if next_inter[0] <= interval[1]:
                            if prev:
                                intervals.remove(prev)
                            prev = next_inter
                        else:
                            break
                    if prev:
                        interval[1] = max(interval[1], prev[1])
                        intervals.remove(prev)
                break

            elif interval[0] >= newInterval[0] and interval[1] <= newInterval[1]:
                interval[1] = max(newInterval[1], interval[1])
                interval[0] = min(newInterval[0], interval[0])

                if idx < len(intervals)-1:
                    prev = None
                    for i, next_inter in enumerate(intervals[idx+1:]):
                        if next_inter[0] <= interval[1]:
                            if prev:
                                intervals.remove(prev)
                            prev = next_inter
                        else:
                            break
                    if prev:
                        interval[1] = max(interval[1], prev[1])
                        intervals.remove(prev)
                break
            
            elif  interval[0] > newInterval[1] and interval[0] >= newInterval[0]:
                intervals.insert(idx, newInterval)
                break

            elif  interval[1] == newInterval[1] and interval[0] >= newInterval[0]:
                interval[0] = newInterval[0]
                break

            elif  interval[1] >= newInterval[1] and interval[0] >= newInterval[0]:
                interval[0] = newInterval[0]
                break
            
            elif interval[1] >= newInterval[0]:
                intervals.insert(idx, newInterval)
                break

            elif idx == len(intervals) - 1:
                intervals.append(newInterval)

        return intervals