class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        full_str = s1 + " " + s2
        word_count = Counter(full_str.split())
        print(word_count)
        ans = []
        
        for key, count in word_count.items():
            if count == 1:
                ans.append(key)
        return ans 
#         s1_words = s1.split()
#         s2_words = s2.split()
#         word_bank = []
        
#         max_num = max(len(s1_words), len(s2_words))
        
#         for i in range(len(s1_words)):
#             if s1_words[i] not in word_bank:
#                 word_bank.append(s1_words[i])
#             else:
#                 word_bank.remove(s1_words[i])
#         print("s1:",word_bank)
            
#         for i in range(len(s2_words)):
#             if s2_words[i] not in word_bank:
#                 word_bank.append(s2_words[i])
#             else:
#                 word_bank.remove(s2_words[i])
#         print("s2:",word_bank)
#         return word_bank
            
        