class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        
        prev_start = intervals[0][0]
        prev_end = intervals[0][1]
        hold_start= hold_end = 0
        ans = []
        ans.append([prev_start, prev_end])
        for start, end in intervals[1:]:
            if start > prev_end:
                prev_end = end
                ans.append([start,end])
            else:
                ans.pop()
                start = min(start,prev_start)
                end = max(prev_end, end)
                ans.append([start,end])
            prev_start = start
            prev_end = end
            
        return ans