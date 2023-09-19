class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        letters = set(word1 + word2)
        arr = []
        for i in letters:
            arr.append(abs(word1.count(i) - word2.count(i)))
        #print(arr)
        
        if max(arr) > 3:
            return False
        else:
            return True