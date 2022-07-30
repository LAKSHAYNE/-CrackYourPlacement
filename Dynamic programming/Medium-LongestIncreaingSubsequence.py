class Solution:
    def __init__(self):
        self.ans=1
    def lengthOfLIS(self, arr: List[int]) -> int:
        n=len(arr)
        temp=[]
        def binaryS(ele):
            start=0
            end=len(temp)-1
            while(start<=end):
                mid=(start+end)//2
                if(ele>temp[mid]):
                    start=mid+1
                elif(ele<temp[mid]):
                    end=mid-1
                else:
                    return mid
            return start
        
        temp=[]
        temp.append(arr[0])
        for i in range(1,len(arr)):
            if(arr[i]>temp[-1]):
                temp.append(arr[i])
            else:
                ind=binaryS(arr[i])
                temp[ind]=arr[i]
        return len(temp)