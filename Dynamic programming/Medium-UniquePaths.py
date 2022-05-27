class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        li=[['X']*n for _ in range(m)]
        li.append([0]*(n+1))
        for i in range(m):
            li[i].append(0)
        li[-2][-1]=1
        #print(li)
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                li[i][j]=li[i+1][j]+li[i][j+1]
        return(li[0][0])
        