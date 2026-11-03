class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m, n = len(grid), len(grid[0])

        def dfs(i, j):

            if i < 0  or i >=m or j <0 or j >=n:
                return True
            
            if grid[i][j]!='1':
                return False
            
            grid[i][j] = '#'

            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)

            return 
        

        v = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    v += 1
        
        return v
            
        