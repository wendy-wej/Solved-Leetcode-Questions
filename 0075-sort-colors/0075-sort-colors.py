class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = list("0" * (nums.count(0)))
        white = list("1" * (nums.count(1)))
        blue = list("2" * (nums.count(2)))
        total = red + white + blue
        total = [int(i) for i in total]
       
        for i in range(len(total)):
            nums[i] = total[i]
        return nums