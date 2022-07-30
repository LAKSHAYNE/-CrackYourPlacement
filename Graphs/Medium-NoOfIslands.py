class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        grid.append(['X']*len(grid[0]))
        grid.insert(0,['X']*len(grid[0]))
        for i in grid:
            i.append('X')
            i.insert(0,'X')
            
        def dfs(row,col,grid):
            if(grid[row][col]=='1'):
                grid[row][col]='2'
                dfs(row+1,col,grid)
                dfs(row-1,col,grid)
                dfs(row,col+1,grid)
                dfs(row,col-1,grid)
            
            
            
        count=0
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                if(grid[i][j]=='1'):
                    count+=1
                    dfs(i,j,grid)
                
        return count