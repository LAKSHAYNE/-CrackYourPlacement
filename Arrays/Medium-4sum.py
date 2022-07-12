class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        res=[]
        i=0
        while(i<n):
            j=i+1
            while(j<n):
                left=j+1
                right=n-1
                a=target-(nums[i]+nums[j])
                while(left<right):
                    temp=nums[left]+nums[right]
                    if(temp<a):
                        left+=1
                    elif(temp>a):
                        right-=1
                    else:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        while(left<right and nums[left]==res[-1][2]):
                            left+=1
                        while(left<right and nums[left]==res[-1][3]):
                            right-=1
                while(j+1<n and nums[j+1]==nums[j]):
                    j+=1
                j+=1    
            while(i+1<n and nums[i+1]==nums[i]):
                i+=1
            i+=1
        return res
                        