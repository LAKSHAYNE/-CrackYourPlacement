import collections
class Solution:
    def __init__(self):
        self.dire='right'
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def def_value():
            return "Not"
        di=collections.defaultdict(def_value)
        maxr=len(matrix)
        maxc=len(matrix[0])
        li=[]
        def dfs(row,col):
            if(row>=maxr or col>=maxc or row<0 or col<0 or di[str(row)+'.'+str(col)]!="Not"):
                if(self.dire=='right'):
                    self.dire='down'
                elif(self.dire=='down'):
                    self.dire='left'
                elif(self.dire=='left'):
                    self.dire='up'
                elif(self.dire=='up'):
                    self.dire='right'
                return
            
            di[str(row)+'.'+str(col)]=1
            li.append(matrix[row][col])
            
            for i in range(maxr//2+1):
                if(self.dire=='right'):
                    dfs(row,col+1)
                if(self.dire=='down'):
                    dfs(row+1,col)
                if(self.dire=='left'):
                    dfs(row,col-1)
                if(self.dire=='up'):
                    dfs(row-1,col)
        
        dfs(0,0)
        return li
        
