class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start=[0,0]
        maxz=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==1):
                    start=[i,j]
                if(grid[i][j]==0):
                    maxz+=1
        
        def f(row,col,maxr,maxcol,visi,nz,maxz):
            # print(row,col,nz,maxz)
            # print(visi[0])
            # print(visi[1])
            # print(visi[2])
            # print('----------')
            if(row<0 or col<0 or row>=maxr or col>=maxcol or grid[row][col]==-1 or visi[row][col]==1):
                return 0
            visi[row][col]=1
            nz+=1
            if(grid[row][col]==2 and nz-2==maxz):
                visi[row][col]=0
                return 1
            dire=[[1,0],[-1,0],[0,1],[0,-1]]
            a=0
            for i in dire:
                a+=f(row+i[0],col+i[1],maxr,maxcol,visi,nz,maxz)
                # if(row+i[0]<0 or col+i[1]<0 or row>=maxr or col>=maxr):
                #     visi[row+i[0]][col+i[1]]=0
                #visi[row][col]=0
            visi[row][col]=0
            nz-=1
            
            return a
        visi=[[0]*len(grid[0]) for _ in range(len(grid))]
        return(f(start[0],start[1],len(grid),len(grid[0]),visi,0,maxz))