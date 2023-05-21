class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        count = min(len(word1), len(word2))
        merge=''
        for i in range(count):
            merge +=word1[i]
            merge+=word2[i]
            if (i == count-1) and (len(word1)>len(word2)):
                merge +=word1[i+1:]
            elif (i == count-1) and (len(word1)<len(word2)):
                merge +=word2[i+1:]
        return merge