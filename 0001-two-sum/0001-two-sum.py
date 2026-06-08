class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_hashmap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in my_hashmap:
                return [i, my_hashmap[diff]]
            else:
                my_hashmap[nums[i]] = i