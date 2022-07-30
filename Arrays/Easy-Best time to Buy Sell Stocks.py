class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        right=1
        left=0
        maxp=0
        
        while right<len(prices):
            currp=prices[right]-prices[left]
            if prices[left]<prices[right]:
                maxp =max(currp,maxp)
            else:
                left=right
            right+=1
        return maxp