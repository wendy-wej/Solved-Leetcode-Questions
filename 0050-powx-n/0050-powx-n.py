class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        
        if n==1:
            return x
        
        abs_n = n
        
        if n<0:
            abs_n = -1 * n
        
        while (abs_n > 0):
            if abs_n % 2 == 0:
                x = x*x
                abs_n = abs_n/2
            else:
                ans *= x
                abs_n -=1
        if n<0:
            ans = 1/ans
            
        return ans
                
                
                
        
        
        # if n ==1:
        #     return 1
        # elif n<0:
        #     return 1 /(x * myPow(-x, n-1))
        # else:
        #     return x * myPow(x, n-1)