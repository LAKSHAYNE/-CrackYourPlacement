class Solution:
    def makeConnected(self, n: int, edges: List[List[int]]) -> int:
        def dfs(n,adj,visi):
            visi[n]=1
            for it in adj[n]:
                if(not visi[it]):
                    dfs(it,adj,visi)
        
        adj=collections.defaultdict(list)
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
        
        
        visi=[0]*n
        comp=0
        for i in range(n):
            if(not visi[i]):
                comp+=1
                dfs(i,adj,visi)
        
        red=len(edges)-((n-1)-(comp-1))
        if(red<comp-1):
            return -1
        else:
            return (comp-1)