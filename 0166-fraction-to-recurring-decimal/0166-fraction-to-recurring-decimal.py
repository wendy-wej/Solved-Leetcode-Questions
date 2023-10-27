class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        quot, rem = divmod(abs(numerator), abs(denominator)) 
        stack = []      
        if numerator * denominator <0 :
            sign = "-"
        else:
            sign = ''
            
        ans =[sign + str(quot), "."]
        
        while rem not in stack:
            stack.append(rem)
            quot, rem = divmod(rem*10, abs(denominator))
            ans.append(str(quot))
            
        idx = stack.index(rem)
        ans.insert(idx+2, '(')
        ans.append(')')
        return ''.join(ans).replace('(0)', '').rstrip('.')
              
        
            
            
                
        
        
        #Unoptimised code is in the notes section