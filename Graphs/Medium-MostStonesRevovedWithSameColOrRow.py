class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n=len(stones)
        maxi=0
        seti=set()
        for i,j in stones:
            seti.add(i)
            seti.add(j+10001)
            maxi=max(maxi,i,j+10001)
        
        parents=[0]*(maxi+1)
        rank=[0]*(maxi+1)
        for i in range(maxi+1):
            parents[i]=i
        
        def findpar(z):
            if(parents[z]==z):
                return z
            return findpar(parents[z])
        
        def union(x,y):
            u=findpar(x)
            v=findpar(y)
            if(rank[u]>rank[v]):
                parents[v]=u
            if(rank[u]==rank[v]):
                parents[v]=u
                rank[u]+=1
            else:
                parents[v]=u
        
        for p,q in stones:
            union(p,q+10001)
        
        count=0
        for i in range(len(parents)):
            if(parents[i]==i and i in seti):
                count+=1
        return len(stones)-count
            