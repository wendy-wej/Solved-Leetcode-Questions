class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        other_half = defaultdict(int)
        ans = 0
        
        for i in time:
            i = i % 60
            if i == 0:
                ans = ans + other_half[0]
            else:
                ans = ans + other_half[(60-i)]
            other_half[i]+=1
        return ans
        
        
        
        
        
#         mod_arr = []
#         pair = 0
        
#         for i in time:
#             mod_arr.append(i%60)
#         print(mod_arr)
        
#         for i in time:
#             time_needed = 60- (i % 60)
#             if time_needed in mod_arr:
#                 time.remove(i)
#         ans = len(mod_arr) - len(time)
#         return ans