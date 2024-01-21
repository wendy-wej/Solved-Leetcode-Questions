class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        
        for i in range(len(s)):
            ans += self.paliCounter(s,i,i)
            ans += self.paliCounter(s,i,i+1)
        return ans
                
    def paliCounter(self, s, l, r):
        ans = 0
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
            ans+=1
        return ans
                
            
            
            

            

        