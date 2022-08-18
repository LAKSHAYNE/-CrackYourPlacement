class NumArray:

    def __init__(self, nums: List[int]):
        n=len(nums)
        st=[0]*(4*n)
        def build(ind,left,right,st):
            if(left==right):
                st[ind]=nums[left]
                return
            mid=int((left+right)//2)
            build(ind*2+1,left,mid,st)
            build(ind*2+2,mid+1,right,st)
            st[ind]=st[ind*2+1]+st[ind*2+2]
        build(0,0,n-1,st)
        self.st=st
        self.nums=nums

    def update(self, i: int, val: int) -> None:
        diff=val-self.nums[i]
        self.nums[i]=val
        def upd(i,left,right,diff,ind):
            if(i<left or i>right):
                return
            if(left==right==i):
                self.st[ind]=val
            if(left!=right):
                self.st[ind]+=diff
                mid=(left+right)//2
                upd(i,left,mid,diff,ind*2+1)
                upd(i,mid+1,right,diff,ind*2+2)
        upd(i,0,len(self.nums)-1,diff,0)

    def sumRange(self, ql: int, qr: int) -> int:
        def sumi(left,right,ind):
            if(right<=qr and left>=ql):
                return self.st[ind]
            if(right<ql or left>qr):
                return 0
            mid=(left+right)//2
            return sumi(left,mid,ind*2+1)+sumi(mid+1,right,ind*2+2)
        
        return sumi(0,len(self.nums)-1,0)
            
            
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)