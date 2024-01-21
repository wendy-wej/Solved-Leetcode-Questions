class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        #Even counter
        
        
        for i in range(len(s)):
            l = r = i
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
                ans+=1
                
            l = i
            r = i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
                ans+=1
        return ans
                
            
            
            

            

        