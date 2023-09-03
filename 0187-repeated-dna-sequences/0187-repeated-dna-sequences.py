class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        word = ''
        start = 0
        end = 10
        word_bank = {}
        ans =set()
        
        while (end <= len(s)):
            word = s[start:end]
            word_bank[word] = 1 + word_bank.get(word, 0)
            if word_bank[word] > 1:
                ans.add(word)
            start+=1
            end+=1
        return ans
            
            
                
            