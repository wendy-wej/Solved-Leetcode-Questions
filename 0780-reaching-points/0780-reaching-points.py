class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while ty>sy and tx>sx:
            tx,ty = tx%ty, ty%tx
            
        return (ty==sy and tx>=sx and (tx-sx)%sy ==0) or (tx==sx and ty>=sy and (ty-sy)%sx == 0)
    
  
            
        # return (sx==tx and ty>=sy and (ty-sy)%sx == 0)  or \
        #         (sy==ty and tx>=sx and (tx-sx)%sy ==0)

    
        
        
        # def reachingPoints(self, sx, sy, tx, ty):
        # while sx < tx and sy < ty:
        #     tx, ty = tx % ty, ty % tx
        # return sx == tx and sy <= ty and (ty - sy) % sx == 0 or \
        #        sy == ty and sx <= tx and (tx - sx) % sy == 0