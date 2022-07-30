class Solution:
    
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V, adj):
		#Code here
		visited=[0]*V
		def check(n,pre):
            visited[n]=1
            q=[[n,pre]]
            while(q):
                node,prev=q.pop()
                for it in adj[node]:
                    if(not visited[it]):
                        q.append([it,node])
                        visited[it]=1
                    else:
                        if(prev!=it):
                            return True
		    
	    for i in range(V):
	        if(not visited[i]):
	            if(check(i,-1)):
	                return True
        return False