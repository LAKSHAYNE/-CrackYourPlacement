class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self,numver, adj):
        # code here
        visited=[0]*(numver)
        bfs=[]
        q=[0]
        visited[0]=1
        while(q):
            node=q.pop(0)
            bfs.append(node)
            for it in adj[node]:
                if(not visited[it]):
                    q.append(it)
                    visited[it]=1
        return bfs