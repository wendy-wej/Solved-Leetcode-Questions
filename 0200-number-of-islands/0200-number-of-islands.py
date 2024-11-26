class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        R = len(grid)
        C = len(grid[0])
        path = set()
        count = 0
        
        def dfs(r,c):
            if (r<0 or c<0 or 
                r>=R or c>=C or 
                grid[r][c]=='0' or (r,c) in path):
                return 
            grid[r][c] = '0'
            path.add((r,c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            path.remove((r,c))
    
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    dfs(r,c)
                    count+=1
        return count
        