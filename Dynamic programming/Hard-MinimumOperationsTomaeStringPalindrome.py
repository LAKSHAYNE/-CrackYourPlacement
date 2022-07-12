import collections
class Solution:
    def minInsertions(self, s: str) -> int:
        def lcs(ind1,ind2,s1,s2,n,dp):
            if(ind1==n or ind2==n):
                return 0
            if(dp[str(ind1)+','+str(ind2)]!=-1):
                return dp[str(ind1)+','+str(ind2)]
            if(s1[ind1]==s2[ind2]):
                dp[str(ind1)+','+str(ind2)]= 1+lcs(ind1+1,ind2+1,s1,s2,n,dp)
                return dp[str(ind1)+','+str(ind2)]
            else:
                dp[str(ind1)+','+str(ind2)]=max(lcs(ind1+1,ind2,s1,s2,n,dp),lcs(ind1,ind2+1,s1,s2,n,dp))
                return dp[str(ind1)+','+str(ind2)] 
        n=len(s)
        def re():
            return -1
        dp=collections.defaultdict(re)
        #return n-lcs(0,0,s,s[::-1],n,dp)
        #Tabulated:--
        s1=s
        s2=s[::-1]
        dpTab=[[0]*(n+1) for i in range(n+1)]
        for ind1 in range(n-1,-1,-1):
            for ind2 in range(n-1,-1,-1):
                if(s1[ind1]==s2[ind2]):
                    dpTab[ind1][ind2]= 1+dpTab[ind1+1][ind2+1]
                else:
                    dpTab[ind1][ind2]=max(dpTab[ind1+1][ind2],dpTab[ind1][ind2+1])
        return n-dpTab[0][0]    






        #MEMORY optimised
        class Solution:
            def minInsertions(self, s: str) -> int:
                n=len(s)
                s1=s
                s2=s[::-1]
                front=[0]*(n+1)
                dpTab=[[0]*(n+1) for i in range(n+1)]
                for ind1 in range(n-1,-1,-1):
                    curr=[0]*(n+1)
                    for ind2 in range(n-1,-1,-1):
                        if(s1[ind1]==s2[ind2]):
                            curr[ind2]= 1+front[ind2+1]
                        else:
                            curr[ind2]=max(front[ind2],curr[ind2+1])
                    front=[*curr]
                return n-front[0]                              