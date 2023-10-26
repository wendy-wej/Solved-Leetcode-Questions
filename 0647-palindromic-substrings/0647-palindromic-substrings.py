class Solution:
    def countSubstrings(self, s: str) -> int:

        ans = len(s)
        ptr = len(s)//2
        
        
        for i in range(1, len(s)):
            j=1
            while i-j >=0 and i+j < len(s) and s[i-j] == s[i+j]:
                ans+=1
                j+=1
                    
             
        for x in range(len(s)): 
            k=0
            while x-k >=0 and x+k+1 < len(s) and s[x-k] == s[x+1+k]:
                ans+=1
                k+=1
            
        return ans
            

        