class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        for i in range(len(nums1)):
            if(nums2[-1]==nums1[i]):
                nums1[i]=-1
            else:
                ind=nums2.index(nums1[i])
                while(ind<len(nums2)-1 and nums2[ind]<=nums1[i]):
                    ind=ind+1
                if(ind==len(nums2)-1):
                    if(nums2[ind]<nums1[i]):
                        nums1[i]=-1
                    else:
                        nums1[i]=nums2[ind]
                else:
                    nums1[i]=nums2[ind]
        return nums1