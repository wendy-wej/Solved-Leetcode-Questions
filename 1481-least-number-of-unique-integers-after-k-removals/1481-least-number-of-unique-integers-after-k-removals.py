class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        my_list = sorted(arr, key = lambda x:(count[x], x))
        return len(set(my_list[k:]))
            
            