class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        
        longest = 0
        for digit in my_set:
            if (digit-1) not in my_set:
                length = 1
                while (digit + length) in my_set:
                    length+=1
                    
                longest = max(length, longest)
        return longest
            
                
        