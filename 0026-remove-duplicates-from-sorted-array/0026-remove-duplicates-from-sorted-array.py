class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 0
        i = 1
        count = 1
        f = len(nums)
        while i < f:
            if nums[x] == nums[i]:
                w = nums.pop(i)
                nums.append(w)
                f-=1
            else:
                count+=1 
                x+=1
                i+=1
        return count
        