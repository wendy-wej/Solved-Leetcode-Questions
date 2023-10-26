class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        j = 0
        for i in range(len(s)):
            ans += self.counter(s, i, i)
            ans += self.counter(s, i, i+1)
        return ans
    
    def counter(self, s, l, r):
        ans = 0
        j=0
        while l-j>=0 and r+j<len(s) and s[l-j]==s[r+j]:
            ans+=1
            j+=1
        return ans
            

#         ans = len(s) 
#         for i in range(len(s)):
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
            

        