class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if(sum(gas)<sum(cost)):
            return -1
        
        diff=0
        start=0
        for i in range(len(gas)):
            diff+=(gas[i]-cost[i])
            if(diff<0):
                diff=0
                start=i+1
        return start
            