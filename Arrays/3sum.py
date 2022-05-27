class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if(nums==[] or nums==[0]):
            return
        nums.sort()
        l=0
        t=len(nums)
        r=t-1
        ans=[]
        for i in range(t):
            l=i+1
            sumi=nums[i]
            r=t-1
            res=[nums[i]]
            while(l<=r):
                print(res)
                if(sumi==0 and res!=[0]):
                    ans.append(res)
                    break
                if(sumi>0):
                    sumi+=nums[l]
                    res.append(nums[l])
                    l+=1
                else:
                    sumi+=nums[r]
                    res.append(nums[r])
                    r-=1
        return ans