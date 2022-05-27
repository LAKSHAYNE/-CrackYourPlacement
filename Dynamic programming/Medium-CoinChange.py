class Solution:
    def __init__(self):
        self.ans=10**6+1   
    def coinChange(self, coins: List[int], amount: int) -> int:
        if(amount==0):
            return 0
        def backt(target,dp):
            if(target in dp):
                return dp[target]
            if(target==0):
                return 0
            dp[target]=float('inf')
            for i in coins:
                if(target-i>=0):
                    dp[target]=min(dp[target],backt(target-i,dp)+1)
            return dp[target]
            
                    
        dp=dict()
        backt(amount,dp)
        return dp[amount] if(amount in dp and dp[amount]!=inf) else -1