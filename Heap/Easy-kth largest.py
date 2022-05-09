import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        t=len(nums)-k
        for i in range(t):
            heapq.heappop(nums)
        return heapq.heappop(nums)