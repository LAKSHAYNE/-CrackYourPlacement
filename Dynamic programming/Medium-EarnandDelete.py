from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count=Counter(nums)
        nums=sorted(count.keys())
        e1=0
        e2=0
        for i in range(len(nums)):
            currE=nums[i]*count[nums[i]]
            if(i>0 and nums[i]-1==nums[i-1]):
                temp=e2
                e2=max(currE+e1,e2)
                e1=temp
            else:
                temp=e2
                e2=currE+e2
                e1=temp
        return e2