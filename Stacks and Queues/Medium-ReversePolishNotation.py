class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for i in tokens:
            if(i!='*' and i!='+' and i!='-' and i!='/'):
                st.append(i)
            else:
                if(i == '+'):
                    st.append(int(st.pop())+int(st.pop()))
                elif(i == '-'):
                    a=int(st.pop())
                    b=int(st.pop())
                    st.append(b-a)
                elif(i == '*'):
                    st.append(int(st.pop())*int(st.pop()))
                elif(i == '/'):
                    a=int(st.pop())
                    b=int(st.pop())
                    st.append(int(b/a))
        
        return st[0]