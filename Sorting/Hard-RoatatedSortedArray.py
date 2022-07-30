class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bins(arr):
            start=0
            end=len(arr)-1
            while(start<=end):
                mid=(start+end)//2
                if(arr[mid]<target):
                    start=mid+1
                elif(arr[mid]>target):
                    end=mid-1
                else:
                    return mid
        
        flag=0
        for i in range(len(nums)-1):
            if(nums[i]>nums[i+1]):
                flag=i
        
        first=bins(nums[:flag+1])
        sec=bins(nums[flag+1:])
        if(first!=None):
            return first
        elif(sec!=None):
            return len(nums[:flag+1])+sec
        else:
            return -1
