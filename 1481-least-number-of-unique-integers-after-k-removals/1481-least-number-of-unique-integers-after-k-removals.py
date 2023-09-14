class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        ctr = Counter(arr)
        keys = sorted(ctr.keys(), key = lambda x: ctr[x])
        for key in keys:
            diff = min(k, ctr[key])
            ctr[key] -= diff
            k -= diff
        res = 0
        for key in ctr:
            if ctr[key] > 0:
                res += 1
        return res
        # count = Counter(arr)
        # my_list = sorted(arr, key = lambda x:(count[x], x))
        # return len(set(my_list[k:]))
            
            