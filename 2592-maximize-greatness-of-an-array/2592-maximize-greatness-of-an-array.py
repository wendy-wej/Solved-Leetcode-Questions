class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        #print(nums)

        ans=0
        l=0
        r=1
        
        while r < len(nums):
            if nums[l] == nums[r]:
                r+=1
            else:
                
                l+=1
                
                r+=1
                
                ans+=1
                
        return ans
        