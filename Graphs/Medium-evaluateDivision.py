class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def build(graph):
            for (u,v),val in zip(equations,values):
                graph[u][v]=val
                graph[v][u]=1/val
        
        graph=collections.defaultdict(dict)
        build(graph)
        
        def dfs(u,v,vis,graph):
            vis[u]=1
            if u not in graph:
                return -1
            if v in graph[u]:
                return graph[u][v]
            
            for i in graph[u]:
                if(not vis[i]):
                    temp=dfs(i,v,vis,graph)
                    if(temp==-1):
                        continue
                    else:
                        return temp*graph[u][i]
            return -1
        
        ans=[]
        for i in queries:
            vis=collections.defaultdict(lambda:0)
            ans.append(dfs(i[0],i[1],vis,graph))
        return  ans
        