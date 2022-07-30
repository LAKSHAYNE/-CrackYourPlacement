
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp=[[[-1 for i in range(len(strs)+1)] for j in range(n+1)] for _ in range(m+1)]
        def count(ad):
            di={'0':0,'1':0}
            for i in ad:
                di[i]+=1
            return di
        def check(index,currm,currn):
            if(dp[currm][currn][index]!=-1):
                return dp[currm][currn][index]
            if(index==len(strs)):
                return 0
            temp=count(strs[index])
            if('0' not in temp):
                temp['0']=0
            if('1' not in temp):
                temp['1']=0
            if(currm-temp['0']>=0 and currn-temp['1']>=0):
                dp[currm][currn][index]=(max(check(index+1,currm,currn),1+check(index+1,currm-temp['0'],currn-temp['1'])))
                return dp[currm][currn][index]
            dp[currm][currn][index]=check(index+1,currm,currn)
            return dp[currm][currn][index]
        return check(0,m,n)