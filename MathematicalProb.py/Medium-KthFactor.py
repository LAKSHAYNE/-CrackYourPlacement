class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        li=[]
        for i in range(1,n+1):
            if(n%i==0):
                li.append(i)
                k-=1
            if(k==0):
                return i
        if(k):
            return -1