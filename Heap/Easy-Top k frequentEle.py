from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if(k==0):
            return
        c=Counter(nums)
        res=[]
        i=0
        for ke in c.most_common():
            res.append(ke[0])
            i+=1
            if(i==k):
                break
        return res