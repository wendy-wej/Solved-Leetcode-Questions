class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_dict = Counter(s)
        for i in char_dict:
            if char_dict[i] == 1:
                return s.index(i)
        return -1
        
        #MY FIRST SOLUTION (VERY SLOW!!)
        # for i in s:
        #     if s.count(i) == 1:
        #         return s.index(i)
        # return -1