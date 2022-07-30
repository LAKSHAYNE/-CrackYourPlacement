from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans=[]
        d=Counter(nums)
        for i in d:
            if(d[i]>1):
                ans.append(i)
        return ans