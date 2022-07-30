import collections
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        di=collections.defaultdict(list)
        dis=[]
        for x,y in points:
            d=x**2+y**2
            di[d].append([x,y])
            heapq.heappush(dis,d)
        
        ans=[]
        for _ in range(k):
            ans.append(di[heapq.heappop(dis)].pop(0))
        return ans