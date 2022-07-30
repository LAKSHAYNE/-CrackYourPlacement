class NumArray:

    def __init__(self, nums: List[int]):
        n=len(nums)
        self.n=n
        segments=[0]*(4*n)
        def s(ind,segments,low,high):
            if(low==high):
                segments[ind]=nums[low]
                return
            mid=(low+high)//2
            s(ind*2+1,segments,low,mid)
            s(ind*2+2,segments,mid+1,high)
            segments[ind]=segments[ind*2+1]+segments[ind*2+2]
        s(0,segments,0,n-1)
        self.segments=segments
        

    def sumRange(self, left: int, right: int) -> int:
        def q(ind,low,high):
            if(high<=right and low>=left):
                return self.segments[ind]
            if(high<left or low>right):
                return 0
            else:
                mid=(high+low)//2
                a=q(ind*2+1,low,mid)
                b=q(ind*2+2,mid+1,high)
                return a+b
        return q(0,0,self.n-1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)