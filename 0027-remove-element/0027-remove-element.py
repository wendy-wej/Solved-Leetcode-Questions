class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        count = 0
        j = len(nums)-1

        if nums == [] or nums == [0]:
            return 0

        while i <= j:
            if i==j and nums[i] == val:
                nums.pop(i)
                break
            elif nums[i] == val:
                nums.pop(i) 
                j-=1
                count +=1
            else:
                i+=1