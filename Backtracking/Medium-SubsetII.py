class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        lent=len(nums)
        nums.sort()
        def backtrack(index,li):
            res.append(li)
            if(index>=lent):
                return
            for i in range(index,lent):
                if(li+[nums[i]] not in res):
                    backtrack(i+1,li+[nums[i]])
        backtrack(0,[])
        return res