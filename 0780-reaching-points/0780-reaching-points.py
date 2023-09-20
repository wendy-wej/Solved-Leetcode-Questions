class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
#         while tx>sx and ty>sy:
#             tx,ty = tx % ty, ty % tx
            
#         return (sx==tx and ty>=sy and (ty-sy)%sx == 0)  or \
#                 (sy==ty and tx>=sx and (tx-sx)%sy ==0)
    
        if sx > tx or sy > ty: return False
        if sx == tx: return (ty-sy)%sx == 0 # only change y
        if sy == ty: return (tx-sx)%sy == 0
        if tx > ty: 
            return self.reachingPoints(sx, sy, tx%ty, ty) # make sure tx%ty < ty
        elif tx < ty: 
            return self.reachingPoints(sx, sy, tx, ty%tx)
        else:
            return False
        
        
        # def reachingPoints(self, sx, sy, tx, ty):
        # while sx < tx and sy < ty:
        #     tx, ty = tx % ty, ty % tx
        # return sx == tx and sy <= ty and (ty - sy) % sx == 0 or \
        #        sy == ty and sx <= tx and (tx - sx) % sy == 0