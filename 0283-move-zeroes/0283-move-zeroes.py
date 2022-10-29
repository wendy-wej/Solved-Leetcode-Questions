class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums) - 1

        if len(nums) > 1:
            while i < j:
                if nums[i] == 0 and nums[i + 1] == 0:
                    nums.pop(i)
                    nums.append(0)
                    j -= 1
                elif nums[i] == 0:
                    nums.pop(i)
                    nums.append(0)
                    i +=1
                    j -= 1
                else:
                    i +=1
                

        return(nums)