from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        count=0
        di=Counter(s)
        s=set()
        for key,freq in di.items():
            while freq in s and freq>0:
                freq-=1
                count+=1
            s.add(freq)
        return count