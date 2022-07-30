class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res=sumi=0
        dic={}
        ans=0
        for i in nums:
            res+=i
            te=res%k
            if(te in dic):
                ans+=dic[te]
                dic[te]+=1
            else:
                dic[te]=1
        return ans