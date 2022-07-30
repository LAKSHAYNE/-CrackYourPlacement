class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        # code here
        maxi=0
        dp=[[0 for i in range(len(S2)+1)] for _ in range(len(S1)+1)]
        for i in range(1,len(S1)+1):
            for j in range(1,len(S2)+1):
                if(S1[i-1]==S2[j-1]):
                    dp[i][j]=1+dp[i-1][j-1]
                    maxi=max(maxi,dp[i][j])
                else:
                    dp[i][j]=0
        return maxi

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n,m = input().strip().split(" ")
        n,m = int(n), int(m)
        S1 = input().strip()
        S2 = input().strip()
        
        
        ob=Solution()
        print(ob.longestCommonSubstr(S1, S2, n, m))
# } Driver Code Ends