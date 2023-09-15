class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #intervals.sort()
        
        # remove = 0
        # prev_end = intervals[0][1]
        # for start, end in intervals[1:]:
        #     if start >= prev_end:
        #         prev_end = end
        #     else:
        #         remove +=1
        #         prev_end = min(end, prev_end)
        # return remove
    
        intervals = sorted(intervals, key = lambda x:x[1])
        remove = 0
        end = -100000
        for i in intervals:
            if i[0] >= end:
                end = i[1]
            else:
                remove += 1
        return remove