class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dis=[float('inf')]*n
        dis[src]=0
        for _ in range(k+1):
            temp=list(dis)
            for it in flights:
                if(dis[it[0]]+it[2]<temp[it[1]]):
                    temp[it[1]]=dis[it[0]]+it[2]
            dis=temp
        
        
        return dis[dst] if(dis[dst]!=float('inf')) else -1