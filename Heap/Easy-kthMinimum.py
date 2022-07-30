import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n=len(matrix)
        new=[]
        for i in range(n):
            new+=matrix[i]
        heapq.heapify(new)
        ans=heapq.heappop(new)
        heapq.heappush(new,ans)
        for i in range(k):
            ans=heapq.heappop(new)
        return ans
        