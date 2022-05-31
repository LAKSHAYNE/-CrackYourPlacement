class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        maxi=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(matrix[i][j]=='1'):
                    maxi=1
                    break
        
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if(matrix[i][j]=='0'):
                    continue
                matrix[i][j]=min(int(matrix[i-1][j]),int(matrix[i-1][j-1]),int(matrix[i][j-1]))+1
                maxi=max(maxi,matrix[i][j])
        
        return maxi**2