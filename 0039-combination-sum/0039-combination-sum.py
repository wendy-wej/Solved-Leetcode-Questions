class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        full_arr = []
        self.dfs(candidates, target, [], full_arr)
        return full_arr
    
    def dfs(self, nums, target, path, full_arr):
        if target < 0:
            return 
        if target == 0:
            full_arr.append(path)
            return 
        for i in range(len(nums)):
            self.dfs(nums[i:], target-nums[i], path+[nums[i]], full_arr)
        