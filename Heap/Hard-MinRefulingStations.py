import heapq
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        maxr=startFuel
        if(maxr>=target):
            return 0
        if(not stations):
            return -1
        if(maxr<stations[0][0]):
            return -1
        pq=[]
        ind=0
        count=0
        while(maxr<target):
            while(ind<len(stations) and maxr>=stations[ind][0]):
                heapq.heappush(pq,[-stations[ind][1],stations[ind][0]])
                ind+=1
            if(not pq):
                return -1
            a=heapq.heappop(pq)
            maxr+=-a[0]
            count+=1
        
        
        
        return count 
                