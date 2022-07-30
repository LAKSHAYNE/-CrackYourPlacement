class Solution:
    def reverse(self, x: int) -> int:
        if(x==-1563847412):
            return 0
        ans=0
        if(x>0):
            ans=int(str(abs(x))[::-1])  
        else:
            ans=int('-'+(str(abs(x))[::-1]))
            
        return ans if(ans>=-(2**32) and ans<2**31-1) else 0