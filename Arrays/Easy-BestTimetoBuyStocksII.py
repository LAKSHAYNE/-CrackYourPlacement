class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        right=1
        li=0
        while(right!=len(prices)):
            currp=prices[right]-prices[left]
            if(currp>0):
                li+=currp
                left=right
                right+=1
            else:
                left=right
                right+=1
        return li
            