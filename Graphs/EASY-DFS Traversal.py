class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        dfsl=[]
        visited=[0]*V
        def dfs(node):
            dfsl.append(node)
            visited[node]=1
            for it in adj[node]:
                if(not visited[it]):
                    dfs(it)
        
        dfs(0)
        return dfsl