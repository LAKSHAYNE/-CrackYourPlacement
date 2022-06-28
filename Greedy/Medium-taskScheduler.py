import heapq
import collections
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if(n==0):
            return len(tasks)
        h=[]
        heapq.heapify(h)
        c=collections.Counter(tasks)
        for k,v in c.items():
            heapq.heappush(h,-v)
        t=0
        q=[]
        while(h or q):
            if(h):
                j=heapq.heappop(h)+1
                if(j!=0):
                    q.append([j,t+n])
            if(q and q[0][1]==t):
                heapq.heappush(h,q[0][0])
                q.pop(0)
            t+=1
                
        return t