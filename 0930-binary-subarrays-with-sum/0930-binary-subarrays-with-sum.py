class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res=defaultdict(int)
        res[0]=1
        ans=0
        prefixsum=0
        for i in nums:
            prefixsum+=i
            ans+=res[prefixsum-goal]
            res[prefixsum]+=1
        return ans
        
        
        
        # count = 0
        # l = 0
        # r = 1
        # val = nums[l] + nums[r]
        # while (r<len(nums)):            
        #     if val == goal:
        #         count+=1
        #         r+=1
        #         if r < len(nums):
        #             val+=nums[r]
        #     if val < goal:
        #         r+=1
        #         val+=nums[r]
        #     if val > goal:
        #         l+=1
        #         val-=nums[l]
        #     print(l,r)
        # return count
            