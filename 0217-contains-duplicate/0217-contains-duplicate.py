class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        else:
            return True
        
'''
Alternative Solution
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
        
        This has a runtime of 131ms and a space complexity of 20mb
'''