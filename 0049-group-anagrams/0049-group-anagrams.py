class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        my_dict = {}

        for i in strs:
            entry = "".join(sorted(i))
            if entry in my_dict:
                my_dict[entry].append(i)
            else:
                my_dict[entry] = [i]
        return(my_dict.values())
            
        