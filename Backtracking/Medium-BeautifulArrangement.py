class Solution:
    def countArrangement(self, n: int) -> int:
        ans=[]
        def backtrack(per,k):
            if(k==n+1):
                ans.append(per)
                return
            for i in range(1,n+1):
                if(i not in per):
                    if(k%i==0 or i%k==0):
                        backtrack(per+[i],k+1)
        backtrack([0],1)
        return(len(ans))