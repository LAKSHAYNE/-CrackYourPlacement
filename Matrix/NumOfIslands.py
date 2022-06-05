def numIslands(grid):
        #code here
        vis=[[0]*len(grid[0]) for _ in range(len(grid))]
        def dfs(row,col):
            if(grid[row][col]==0 or row>=len(grid) or col>=len(grid[0]) or row<0 or col<0 or vis[row][col]==1):
                return
            else:
                vis[row][col]=1
                dfs(row+1,col)
                dfs(row-1,col)
                dfs(row,col-1)
                dfs(row,col+1)
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(not vis[i][j]):
                    count+=1
                    dfs(i,j)
        
        return count

numIslands([[0,1],[1,0]])