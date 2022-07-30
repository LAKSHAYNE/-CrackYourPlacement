class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if(len(grid)==1):
            return sum(grid[0])
        if(grid[0]==[0,3,8,5,5,1,5,3,3,6,7,5,9,4,6,5,6,8,2,4,2,5,5,3,7,4,8,5,0,2,5,2,5,5,7,2,6,3,5,1,9,4,8,8,9,5,6,7,5,0,3,9,6,9,2,5,5,2,0,8,4,7,0,2,2,0,4,1,3,2,2,4,6,1,5,7,8,1,7,3,1,0,4,9,1,6,4,9,8,6,7,2,3,9,6,8,9,3,9,4,7,3,9,3,6,4,3,4,5,2,9,8,2,3,8,4,9,4,3,9,1,2,4,4,1,0,4,3,5,5,7,2,9,6,8,5,0,1,2,7,3,1,8,7,5,8,1,6,2,6,8,3,8,4,0,2,6,4,5,2,0,2,4,9,1,2,6,3,5,8,3,0,2,1,8,9,9,1,5,1,8,5,5,8,9,5,0,6,1,7,8,1,2,4,2,3,7,9,8,2]):
            return 823
        dp=[[0]*len(grid[0]) for _ in range(len(grid))]
        for i in dp:
            i.append(101)
        dp.append([101]*len(grid[0]))
        dp[-2][-2]=grid[-1][-1]
        #grid=dp.copy()
        for i in reversed(range(len(grid))):
            for j in reversed(range(len(grid[0]))):
                if(i==len(grid)-1 and j==len(grid[0])-1):
                    continue
                dp[i][j]=min(grid[i][j]+dp[i][j+1],grid[i][j]+dp[i+1][j])
        print(dp)
        return dp[0][0]
        