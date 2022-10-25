class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low_index = 0
        high_index = len(nums) - 1
        
        while low_index <= high_index:
            mid_index = low_index + ((high_index - low_index)//2)
            midpoint = nums[mid_index]
            
            if target not in nums:
                return -1
            
            elif target == midpoint:
                return mid_index
            
            elif target >= midpoint:
                low_index = mid_index + 1
            
            else:
                high_index = mid_index - 1
                    
        return 
        