class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        for i in range(len(chars)-1,-1,-1):
            if i and chars[i]==chars[i-1]:
                count += 1
                chars.pop(i)
            else:
                if count>1:
                    for item in str(count)[::-1]:
                        chars.insert(i+1, item)
                    count = 1
                
       
        

        
        
        
#         slow= 0
#         fast = 0
        
#         while fast < len(chars):
#             chars[slow] = chars[fast]
#             count = 1
            
#             while fast+1 < len(chars) and chars[fast] == chars[fast+1]:
#                 count+=1
#                 fast+=1
                
#             if count>1:    
#                 for i in str(count):
#                     chars[slow+1]= i
#                     slow+=1
                    
#             slow+=1
#             fast+=1
            
#         return slow
                
        
                
                
            
            
            
            

            

        
                
            
        