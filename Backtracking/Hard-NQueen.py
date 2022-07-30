class Solution:
    def __init__(self):
        self.ans=[]
    def solveNQueens(self, n: int) -> List[List[str]]:
        def solve(col,board,ans,left,lowerDia,upperDia):
            if(col==n):
                self.ans.append(board.copy())
                return
            
            for row in range(n):
                if(left[row]==0 and lowerDia[row+col]==0 and upperDia[(n-1)-row+col]==0):
                    board[row]=board[row][:col]+'Q'+board[row][col+1:]
                    left[row]=1
                    lowerDia[row+col]=1
                    upperDia[(n-1)-row+col]=1
                    solve(col+1,board,ans,left,lowerDia,upperDia)
                    board[row]=board[row][:col]+'.'+board[row][col+1:]
                    left[row]=0
                    lowerDia[row+col]=0
                    upperDia[(n-1)-row+col]=0
            
            
        
        board=['.'*n for _ in range(n)] 
        lowD=[0]*(2*n-1)
        uppD=[0]*(2*n-1)
        left=[0]*n
        ans=[]
        solve(0,board,ans,left,lowD,uppD)
        return self.ans