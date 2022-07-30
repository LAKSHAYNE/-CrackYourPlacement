#User function Template for python3

class Solution:
	def isNegativeWeightCycle(self, n, edges):
		#Code here
		dis=[float('inf')]*n
		dis[0]=0
	    for _ in range(n-1):
	        for it in edges:
	            if(dis[it[0]]+it[2]<dis[it[1]]):
	                dis[it[1]]=dis[it[0]]+it[2]
	        

        for it in edges:
            if(dis[it[0]]+it[2]<dis[it[1]]):
                return 1
	        
        return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n)
		m = int(m)
		edges = []
		for _ in range(m):
			edges.append(list(map(int, input().split())))
		obj = Solution()
		ans = obj.isNegativeWeightCycle(n, edges)
		print(ans)

# } Driver Code Ends