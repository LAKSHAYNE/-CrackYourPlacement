class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero=0
        one=0
        i=0
        while(len(nums)>i):
            if(nums[i]==0):
                nums[zero],nums[i]=nums[i],nums[zero]
                zero+=1
                i=zero
                one=i
            elif(nums[i]==1):
                nums[one],nums[i]=nums[i],nums[one]
                one+=1
                i=one
            else:
                i+=1
        