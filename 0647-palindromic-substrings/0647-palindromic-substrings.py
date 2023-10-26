class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            res += self.countPali(s, i, i)
            res += self.countPali(s, i, i + 1)
        return res

    def countPali(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res
#         ans = len(s)
#         ptr = len(s)//2
        
        
#         for i in range(1, len(s)):
#             j=1
#             while i-j >=0 and i+j < len(s) and s[i-j] == s[i+j]:
#                 ans+=1
#                 j+=1
                    
             
#         for x in range(len(s)): 
#             k=0
#             while x-k >=0 and x+k+1 < len(s) and s[x-k] == s[x+1+k]:
#                 ans+=1
#                 k+=1
            
#         return ans
            

        