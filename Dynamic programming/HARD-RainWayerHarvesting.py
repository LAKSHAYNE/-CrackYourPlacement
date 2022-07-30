class Solution:
    def trap(self, heights: List[int]) -> int:
        n=len(heights)
        l,r=0,n-1
        lmax=heights[l]
        rmax=heights[r]
        vol=0
        while(l<r):
            lmax,rmax=max(lmax,heights[l]),max(rmax,heights[r])
            if(lmax<rmax):
                vol+=lmax-heights[l]
                l+=1
            else:
                vol+=rmax-heights[r]
                r-=1
        return vol