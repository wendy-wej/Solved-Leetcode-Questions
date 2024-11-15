class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])
        path = set()
        
        def dfs(r,c,i):
            if i == len(word):
                return True
            
            if (r < 0 or c < 0 or
               r >= R or c>=C or
               (r,c) in path or
               word[i] != board[r][c]):
                return False
            
            path.add((r,c))
            ans = (dfs(r+1, c, i+1) or
                  dfs(r-1, c,  i+1) or
                  dfs(r,  c+1, i+1) or
                  dfs(r,  c-1,  i+1) )
            path.remove((r,c))
            return ans
        
        count = {}
        for c in word:
            count[c] = 1 + count.get(c, 0)
        
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
            
        for r in range(R):
            for c in range(C):
                if dfs(r,c,0):
                    return True
                
        return False
         
            
            
        