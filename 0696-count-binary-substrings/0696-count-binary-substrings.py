class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev, curr = 0,1
        count = 0
        
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                curr +=1
            else:
                count += min(prev, curr)
                prev = curr
                curr = 1
        count += min(prev, curr)
        return count
        
        
        
        
        # prevCount = 0
        # otherCount = 1
        # prev = s[0]
        # ans =0
        # for i in range(1, len(s)):
        #     if prev == s[i]:
        #         otherCount +=1
        #     else:
        #         ans += min(prevCount, otherCount)
        #         prevCount = otherCount
        #         otherCount = 1
        #     prev = s[i]
        # ans += min(prevCount, otherCount)
        # return ans
                