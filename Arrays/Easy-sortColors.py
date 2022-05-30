class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start=0
        end=len(nums)
        for i in range(end-1):
            for j in range(end-1-i):
                if(nums[j]>nums[j+1]):
                    nums[j],nums[j+1]=nums[j+1],nums[j]
    
        