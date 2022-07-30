import collections
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def f(ind,buy,count,n,dp):
            if(ind==n or count==0):
                return 0
            if(dp[str(ind)+','+str(buy)+','+str(count)]!=-1):
                return dp[str(ind)+','+str(buy)+','+str(count)]
            if(buy):
                dp[str(ind)+','+str(buy)+','+str(count)]= max(-prices[ind]+f(ind+1,0,count,n,dp),f(ind+1,1,count,n,dp))
                return dp[str(ind)+','+str(buy)+','+str(count)]
            else:
                dp[str(ind)+','+str(buy)+','+str(count)]= max(prices[ind]+f(ind+1,1,count-1,n,dp),f(ind+1,0,count,n,dp))
                return dp[str(ind)+','+str(buy)+','+str(count)]
        
        def re():
            return -1
        dp=collections.defaultdict(re)
        #return f(0,1,k,len(prices),dp)
        #TABULATION:---
        n=len(prices)
        maxi=0
        dpTab=[[[0 for f in range(k+1)] for w in range(2)] for q in range(n+1)]
        for i in range(n-1,-1,-1):
            for j in range(2):
                for c in range(1,k+1):
                    if(j==1):
                        dpTab[i][j][c]= max(-prices[i]+dpTab[i+1][0][c],dpTab[i+1][1][c])
                    else:
                        dpTab[i][j][c]= max(prices[i]+dpTab[i+1][1][c-1],dpTab[i+1][0][c])
        
        return dpTab[0][1][k]
                                         
                                         