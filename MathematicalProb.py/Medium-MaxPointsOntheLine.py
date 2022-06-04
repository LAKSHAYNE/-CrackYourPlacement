class Solution:
    def maxPoints(self, p: List[List[int]]) -> int:
        n=len(p)
        if(n<2):
            return 1
        maxi=2
        for i in range((n)):
            for j in range(i+1,(n)):
                total=2
                for k in range((n)):
                    if(k!=i and k!=j):
                        if((p[j][1]-p[i][1])*(p[i][0]-p[k][0])==(p[i][1]-p[k][1])*(p[j][0]-p[i][0])):
                            total+=1
                maxi=max(total,maxi)
        return maxi