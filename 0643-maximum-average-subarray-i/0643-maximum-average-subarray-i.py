class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        avg = maxAvg = sum(nums[:k])
        
        for r in range(k, len(nums)):
            avg += nums[r]
            avg -= nums[r-k]
            maxAvg = max(maxAvg, avg)
        return maxAvg/k
            
            
            
        