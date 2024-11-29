class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:           
        if not grid:
            return 0
        
        R = len(grid)
        C = len(grid[0])
        count = 0
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    self.dfs(grid, r,c)
                    count+=1
        return count
    
    def dfs(self, grid, r,c):
        R = len(grid)
        C = len(grid[0])
        if (r<0 or c<0 or 
            r>=R or c>=C or 
            grid[r][c]=='0'):
            return 
        grid[r][c] = '0'

        self.dfs(grid, r+1, c)
        self.dfs(grid, r-1, c)
        self.dfs(grid, r, c+1)
        self.dfs(grid, r, c-1)
        