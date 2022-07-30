#User function Template for python3

class Solution:
    def isKPartitionPossible(self, a, k):
        #code here
        sumi=sum(a)
        if(sumi%k!=0):
            return False
        target=int(sumi/k)
        #print('target>>>',target)
        visi=[False]*len(a)
        
        def backtrack(ind,k,subsetsum):
            #print(ind,k,subsetsum,visi)
            if(k==0):
                return True
            if(subsetsum==target):
                return backtrack(0,k-1,0)
            
            for i in range(ind,len(a)):
                if(visi[i] or subsetsum+a[i]>target):
                    continue
                visi[i]=True
                if backtrack(i+1,k,subsetsum+a[i]):
                    return True
                visi[i]=False
            return False

        return backtrack(0,k,0)
#{ 
 # Driver Code Starts


if __name__ == '__main__':
    tcs = int(input())
    for _ in range(tcs):
        N=int(input())
        arr=[int(x) for x in input().split()]
        k=int(input())
        if Solution().isKPartitionPossible(arr, k):
            print(1)
        else:
            print(0)
# } Driver Code Ends