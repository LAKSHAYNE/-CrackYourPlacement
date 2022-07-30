class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        maxr=len(matrix)
        maxc=len(matrix[0])
        if(maxr==1 and maxc==1):
            return 1
        
        
        def f(r,c,prev,visi,dp):
            if(r<0 or c<0 or r>=maxr or c>=maxc or prev<matrix[r][c] or prev==matrix[r][c] or visi[r][c]):
                return 0
            visi[r][c]=1
            if(dp[str(r)+','+str(c)]!=-1):
                return dp[str(r)+','+str(c)]
            direc=[[-1,0],[1,0],[0,1],[0,-1]]
            a=0
            for i in direc:
                newr=i[0]+r
                newc=i[1]+c
                a=max(a,1+f(newr,newc,matrix[r][c],visi,dp))
            visi[r][c]=0
            dp[str(r)+','+str(c)]=max(a,dp[str(r)+','+str(c)])
            return dp[str(r)+','+str(c)]
        
        
        maxi=0
        dp=collections.defaultdict(lambda :-1)
        for i in range(maxr):
            for j in range(maxc):
                visi=[[0]*maxc for _ in range(maxr)]
                maxi=max(maxi,f(i,j,2**32,visi,dp))
                
        return maxi  