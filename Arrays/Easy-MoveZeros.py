class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        for _ in nums:
            if(nums[i]==0):
                nums.pop(i)
                nums.append(0)

            else:
                i+=1
        