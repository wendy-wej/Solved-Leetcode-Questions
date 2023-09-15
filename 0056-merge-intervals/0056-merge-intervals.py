class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        
        for start, end in intervals[1:]:
            prev_start = ans[-1][0]
            prev_end = ans[-1][1]
            if start > prev_end:
                ans.append([start, end])
            else:
                ans[-1] = [min(start, prev_start),max(end, prev_end)]
        return ans

    #<-----------------ALTERNATIVE SOLUTION ------------>
    
#         intervals.sort()     
#         prev_start = intervals[0][0]
#         prev_end = intervals[0][1]
#         ans= []
#         ans.append([prev_start, prev_end])
        
#         for start, end in intervals[1:]:
#             if start > prev_end:
#                 ans.append([start, end])
#                 prev_end = end
#             else:
#                 ans.pop()
#                 start = min(start, prev_start)
#                 end = max(end, prev_end)
#                 ans.append([start, end])
#             prev_start = start
#             prev_end = end
#             #print(ans)
#         return ans