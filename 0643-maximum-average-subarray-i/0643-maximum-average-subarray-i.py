class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = maxTotal = sum(nums[0:k])
        
        for r in range(k, len(nums)):
            total+= nums[r]
            total-= nums[r-k]
            maxTotal = max(total, maxTotal)
        return maxTotal/k