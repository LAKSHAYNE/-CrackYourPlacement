class Solution:
    def removeKdigits(self, s: str, k: int) -> str:
        if(k==len(s)):
            return '0'
        st=[s[0]]
        for i in s[1:]:
            while(st and int(i)<int(st[-1]) and k>0):
                st.pop()
                k-=1
            st.append(i)
        if(k>0):
            st=st[:len(st)-k]
        return str(int(''.join(st)))