import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        identifier = set(nums)
        my_dict ={}
        for num in identifier:
            my_dict[num] = nums.count(num)
        
        
        answer = heapq.nlargest(k, my_dict, key=my_dict.get)
        return answer
            
                
        