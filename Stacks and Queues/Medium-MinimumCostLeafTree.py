import copy
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        st=[float('inf')]
        res=0
        for i in arr:
            while(st and st[-1]<=i):
                mid=st.pop()
                res+=mid*min(st[-1],i)
            st.append(i)
        while(len(st)>2):
            res+=(st.pop()*st)
        
        
        return res
                    