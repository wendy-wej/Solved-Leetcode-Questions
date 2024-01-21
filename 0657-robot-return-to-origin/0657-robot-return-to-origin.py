class Solution:
    def judgeCircle(self, moves: str) -> bool:
        ## count the no of each step and ensure that opposing directions cancel out
        
        u = moves.count('U')
        d = moves.count('D')
        l = moves.count('L')
        r = moves.count('R')

        return u==d and l==r
    
        #return (moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R"))
            
        
        
        
        # <------------ Alternative but slower solution -------------->
#         l_r = 0
#         u_d = 0
#         for i in moves:
#             if i == 'R':
#                 l_r +=1
#             elif i == 'L':
#                 l_r -=1
#             elif i == 'U':
#                 u_d -=1
#             elif i == 'D':
#                 u_d +=1
            
#         return l_r == 0 and u_d ==0
        