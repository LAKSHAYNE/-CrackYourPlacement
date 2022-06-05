class Solution:
	def isBipartite(self, V, adj):
		#code here
		n=len(adj)
		visi=[-1]*n
		for i in range(n):
		    if(visi[i]==-1):
		        q=[i]
		        visi[i]=1
		        while(q):
		            node=q.pop(0)
	                for it in adj[node]:
	                    if(visi[it]==-1):
	                        visi[it]=1-visi[node]
	                        q.append(it)
	                    else:
	                        if(visi[it]==visi[node]):
	                            return 0
        return 1

#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for i in range(E):
			u, v = map(int, input().strip().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isBipartite(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends