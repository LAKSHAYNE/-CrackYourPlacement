class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum={0:1}
        sumi=0
        res=0
        for i in nums:
            sumi+=i
            diff=sumi-k
            res+=prefixSum.get(diff,0)
            prefixSum[sumi]=1+prefixSum.get(sumi,0)
        return res