class Solution:
    def minFlips(self, target: str) -> int:
        prev = "0"
        ans = 0
        for bit in target:
            if prev != bit:
                ans+=1
            prev = bit
            
        return ans
        
         