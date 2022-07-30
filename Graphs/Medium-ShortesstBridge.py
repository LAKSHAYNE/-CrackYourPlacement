class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        queue=[]
        visi=[[0 for i in range(len(grid[0]))] for _ in range(len(grid))]
        dirs=[[0,-1],[0,1],[1,0],[-1,0]]
        def bfs():
            roun=0
            while(queue):
                count=len(queue)
                roun+=1
                for _ in range(count):
                    node=queue.pop(0)
                    for i in dirs:
                        rowd=node[0]+i[0]
                        cold=node[1]+i[1]

                        if(rowd<0 or cold<0 or rowd>=len(grid) or cold>=len(grid[0])):
                            continue
                        else:
                            if(grid[rowd][cold]==1 and not visi[rowd][cold]):
                                return roun
                            elif(not visi[rowd][cold]):
                                grid[rowd][cold]=1
                                visi[rowd][cold]=1
                                queue.append([rowd,cold])
                
        
        
        def dfs(row,col):
            if(row<0 or col<0 or row>=len(grid) or col>=len(grid[0]) or grid[row][col]==0 or visi[row][col]):
                return
            queue.append([row,col])
            visi[row][col]=1
            for i in dirs:
                dfs(row+i[0],col+i[1])
            
        flag=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==1):
                    dfs(i,j)
                    flag=1
                    break
            if(flag):
                break
                
        dfs(0,0)
        return(bfs()-1)
        