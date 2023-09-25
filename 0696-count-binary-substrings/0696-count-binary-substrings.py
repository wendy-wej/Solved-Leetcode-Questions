class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prevCount = 0
        otherCount = 1
        prev = s[0]
        ans =0
        for i in range(1, len(s)):
            if prev == s[i]:
                otherCount +=1
            else:
                ans += min(prevCount, otherCount)
                prevCount = otherCount
                otherCount = 1
            prev = s[i]
        ans += min(prevCount, otherCount)
        return ans
                