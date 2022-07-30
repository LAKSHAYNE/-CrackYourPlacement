class Solution:
    def solveSudoku(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def validate(num,row,col):
            for i in range(9):
                if str(num) == grid[row][i]: return False
                if str(num) == grid[i][col]: return False
                if str(num) == grid[3*(row//3) +i//3][3*(col//3) +i%3]: return False
            return True
            
        def f():
            for r in range(9):
                for c in range(9):
                    if(grid[r][c]=='.'):
                        for i in range(1,10):
                            if(validate(i,r,c)):
                                grid[r][c]=str(i)
                                if(f()):
                                    return True
                                else:
                                    grid[r][c]='.'
                        return False
            return True
        
        f()