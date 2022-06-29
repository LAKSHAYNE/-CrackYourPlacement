class Solution:
    def __init__(self):
        self.mx=0
    def numOfMinutes(self, n: int, headID: int, manager: List[int], edj: List[int]) -> int:
        adj=[[] for _ in range(n)]
        for i in range(n):
            if(manager[i]==-1):
                continue
            adj[i].append(manager[i])
            adj[manager[i]].append(i)
        
        
        def dfs(node,visi,count):
            self.mx=max(self.mx,count)
            visi[node]=1
            for it in adj[node]:
                if(not visi[it]):
                    dfs(it,visi,count+edj[node])
        visi=[0]*n
        maxi=0
        start=manager.index(-1)
        dfs(start,visi,0)
        return self.mx