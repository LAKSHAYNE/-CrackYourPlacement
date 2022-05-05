class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1+=nums2
        nums1.sort()
        i=0
        while(nums1[i]==0 or nums1[i]<0):
            if(len(nums1)==m+n):
                break
            if(nums1[i]<0):
                i+=1
            elif(nums1[i]==0):
                nums1.pop(i)
        