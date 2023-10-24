# class Solution:
#     def sortByBits(self, arr: List[int]) -> List[int]:
#         arr.sort(key = lambda x: (x.bit_count(), x))
#         return arr
        
        
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count_set_bits(number):
            count = 0
            while number:
                count += number & 1
                number >>= 1
            return count
            
            #return weight
        
        arr.sort(key = lambda num: (count_set_bits(num), num))
        return arr