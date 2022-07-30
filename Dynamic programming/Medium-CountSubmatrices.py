class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if(matrix[i][j]==0):
                    continue
                else:
                    matrix[i][j]=min(matrix[i-1][j],matrix[i-1][j-1],matrix[i][j-1])+1
                
        sumi=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                sumi+=matrix[i][j]
        
        return sumi
                