import collections
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj=collections.defaultdict(list)
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)
        visi=[0]*n
        low=[0]*n
        tin=[0]*n
        def dfs(node,timer,low,tin,parent,bridge):
            visi[node]=1
            low[node]=tin[node]=timer
            for it in adj[node]:
                if(it==parent):
                    continue
                if(not visi[it]):
                    dfs(it,timer+1,low,tin,node,bridge)
                    low[node]=min(low[node],low[it])
                    if(low[it]>tin[node]):
                        bridge.append([node,it])
                else:
                    low[node]=min(tin[it],low[node])
        
        bridge=[]
        dfs(0,1,low,tin,-1,bridge)
        return bridge
                    