class Solution:
    def knightDialer(self, n: int) -> int:
        if(n==1):
            return 10
        adj=[[4,6],[6,8],[7,9],[8,4],[3,9,0],[],[1,7,0],[2,6],[1,3],[2,4]]
        mod=10**9+7
        def tab():
            dpTab=[[0 for i in range(10)] for _ in range(n)]
            for i in range(10):
                dpTab[0][i]=1
            for i in range(1,n):
                for curr in range(10):
                    if(curr==5):
                        continue
                    a=0
                    for j in adj[curr]:
                        a=(a+dpTab[i-1][j])%mod
                    dpTab[i][curr]=a%mod
            return sum(dpTab[n-1])%mod
        return tab()