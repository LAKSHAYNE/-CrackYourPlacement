class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd=intervals[0][1]
        re=0
        for start,end in intervals[1:]:
            if(prevEnd<=start):
                prevEnd=end
            else:
                prevEnd=min(end,prevEnd)
                re+=1
        return re