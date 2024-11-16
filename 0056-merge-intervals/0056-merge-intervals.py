class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i:i[0])
        ans = [intervals[0]]
        
        for i in range(1, len(intervals)):
            last = ans[-1]
            if last[1] < intervals[i][0]:
                ans.append(intervals[i])
            else:
                ans[-1][1] =max(last[1], intervals[i][1])
        return ans
                
        