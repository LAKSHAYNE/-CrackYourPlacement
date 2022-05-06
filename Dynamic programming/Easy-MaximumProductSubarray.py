class Solution:
    def maxProduct(self, nums: List[int]) -> int:        
        res=max(nums)
        currmin,currmax=1,1
        for i in range(len(nums)):
            if(nums[i]==0):
                currmin,currmax=1,1
            else:
                temp=currmax
                currmax=max(currmax*nums[i],currmin*nums[i],nums[i])
                currmin=min(temp*nums[i],currmin*nums[i],nums[i])
                res=max(res,currmax)
                
        return res