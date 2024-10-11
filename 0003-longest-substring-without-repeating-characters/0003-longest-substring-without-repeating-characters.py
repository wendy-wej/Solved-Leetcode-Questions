class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_num = 0
        letter = set()
        
        for r in range(len(s)):
            while s[r] in letter:
                letter.remove(s[l])
                l+=1
            letter.add(s[r])
            max_num = max(max_num, (r-l+1))
        return max_num