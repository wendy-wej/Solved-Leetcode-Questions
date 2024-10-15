class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        l=0
        r=0
        ans = 0
        nums.sort()
        while r < len(nums):
            if nums[r] > nums[l]:
                l+=1
                ans+=1
            r+=1
        return ans
            
        