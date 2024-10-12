class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        word_dict = dict()
        ans = 0
        l = r = 0
        maxf = 0
        for r in range(len(s)):
            if s[r] in word_dict:
                word_dict[s[r]] +=1
            else: 
                word_dict[s[r]] = 1
                
            maxf = max(maxf, word_dict[s[r]] )
            while (r-l+1) - maxf > k:
                word_dict[s[l]] -=1
                l+=1
            ans = max(ans, r-l+1)    
        return ans
            
                
        