class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def f(ind,li,ans):
            ans.append(li)
            for i in range(ind,len(nums)):
                f(i+1,li+[nums[i]],ans)
                
        ans=[]
        f(0,[],ans)
        return ans