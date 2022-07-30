class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=len(list(set(nums)))
        j=0
        i=1
        while i!=k:
            if(nums[j]==nums[i]):
                nums.pop(i)
            else:
                j+=1
                i+=1
        print(nums)
        return k
        