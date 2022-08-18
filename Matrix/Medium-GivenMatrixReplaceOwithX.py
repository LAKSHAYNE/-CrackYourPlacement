#User function Template for python3

class Solution:
    def fill(self, n, m, mat):
        def dfs(r,c):
            if(r<0 or r>=n or c<0 or c>=m):
                return
            if(mat[r][c]=='O'):
                return
            if(mat[r][c]=='-'):
                mat[r][c]='O'
            if(mat[r][c]=='X'):
                return
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r,c+1)
            
        
        for i in range(n):
            for j in range(m):
                if(mat[i][j]=='O'):
                    mat[i][j]='-'
        
        for i in range(m):
            if(mat[n-1][i]=='-'):
                dfs(n-1,i)
        
        for i in range(m):
            if(mat[0][i]=='-'):
                dfs(0,i)
        
        for i in range(n):
            if(mat[i][0]=='-'):
                dfs(i,0)
        
        for i in range(n):
            if(mat[i][m-1]=='-'):
                dfs(i,m-1)
        
        for i in range(n):
            for j in range(m):
                if(mat[i][j]=='-'):
                    mat[i][j]='X'
        
        return mat

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = []
        for i in range(n):
            s = list(map(str,input().split()))
            mat.append(s)
        
        ob = Solution()
        ans = ob.fill(n, m, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end = " ")
            print()
# } Driver Code Ends