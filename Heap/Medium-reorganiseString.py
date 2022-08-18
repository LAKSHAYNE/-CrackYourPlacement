import collections
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        c=Counter(s)
        maxheap=[[-cnt,char] for char,cnt in c.items()]
        heapq.heapify(maxheap)
        prev=None
        res=''
        while(maxheap or prev):
            if(prev and not maxheap):
                return ''
            a=heapq.heappop(maxheap)
            res+=a[1]
            a[0]+=1
            if(prev):
                heapq.heappush(maxheap,prev)
                prev=None
            if(a[0]!=0):
                prev=a
        return res
                