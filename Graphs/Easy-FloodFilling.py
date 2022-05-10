class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        if(image[sr][sc]==newColor):
            return image
        def dfs(row,col,value,maxr,maxc):
            if(row<0 or col<0 or row>=maxr or col>=maxc or image[row][col]!=value):
                return
            else:
                image[row][col]=newColor
                dfs(row+1,col,value,maxr,maxc)
                dfs(row-1,col,value,maxr,maxc)
                dfs(row,col+1,value,maxr,maxc)
                dfs(row,col-1,value,maxr,maxc)
        
        dfs(sr,sc,image[sr][sc],len(image),len(image[0]))
        return(image)