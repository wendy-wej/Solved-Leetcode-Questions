class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left_ptr= 0
        total= 0
        min_size = float('inf')
               
        for right_ptr in range(len(nums)):
            total += nums[right_ptr]
            while total>= target:
                min_size = min(min_size, (right_ptr-left_ptr+1))
                total -= nums[left_ptr]
                left_ptr+=1
                
        return min_size if min_size != float('inf') else 0
        