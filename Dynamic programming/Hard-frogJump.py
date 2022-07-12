class Solution:
    def canCross(self, nums: List[int]) -> bool:
        def f(ind,prevJump,adj,dp,ch):
            if(ind==len(nums)-1):
                return True
            if(dp[str(ind)+','+str(prevJump)]!=-1):
                return dp[str(ind)+','+str(prevJump)]
            if(ind>=len(nums)):
                return False
            j1=prevJump-1
            j2=prevJump
            j3=prevJump+1
            a=b=c=False
            if(j1>0 and j1+nums[ind] in ch):
                a=f(adj[j1+nums[ind]],j1,adj,dp,ch)
            if(j2>0 and j2+nums[ind] in ch):
                b=f(adj[j2+nums[ind]],j2,adj,dp,ch)
            if(j3>0 and j3+nums[ind] in ch):
                c=f(adj[j3+nums[ind]],j3,adj,dp,ch)
            dp[str(ind)+','+str(prevJump)]= a or b or c
            return dp[str(ind)+','+str(prevJump)]
        
        adj={}
        ch=set(nums)
        def re():
            return -1
        dp=collections.defaultdict(re)
        for i,val in enumerate(nums):
            adj[val]=i
            
        return f(0,0,adj,dp,ch)
        