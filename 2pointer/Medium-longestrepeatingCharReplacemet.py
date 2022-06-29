import collections
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        c={}
        long=0
        for r in range(len(s)):
            c[s[r]]=1+c.get(s[r],0)
            maxc=max(c.values())
            if(r-l+1-maxc<=k):
                long=r-l+1
            else:
                c[s[l]]-=1
                l+=1
        return long