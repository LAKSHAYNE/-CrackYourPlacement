class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        st=0
        en=len(nums)-1
        mi=[]
        def bubb(start,end,mi):
            if(start>end):
                return
            if(start==end):
                mi.append(start)
                return 
            mid=(start+end)//2
            if(nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]):
                mi.append(mid)
                return mid
            else:
                bubb(start,mid-1,mi)
                bubb(mid+1,end,mi)
        bubb(st,en,mi)
        maxr=nums[mi[0]]
        ind=mi[0]
        #print(mi)
        for i in mi:
            if(nums[i]>maxr):
                maxr=nums[i]
                ind=i
        return ind