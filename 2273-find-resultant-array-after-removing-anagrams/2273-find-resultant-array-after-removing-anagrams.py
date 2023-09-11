class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = [words[0]]
        for i in range(len(words)-1):
            if Counter(words[i]) != Counter(words[i+1]):
                ans.append(words[i+1])
        return ans
            
                
            
            
            
            
            
#         new_words = ['ab'] * len(words)
#         for i in range(len(words)):
#             new_words[i] = ''.join(sorted(words[i]))
#             #print(words)
        
#         for i in range(len(words)-1):
#             if new_words[i] == new_words[i+1]:
#                 del new_words[i]
#                 del words[i]
            
#         return words