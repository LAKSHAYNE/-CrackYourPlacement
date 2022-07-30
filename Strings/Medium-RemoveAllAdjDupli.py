class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk=[]
        for i in s:
            if stk and stk[-1][0]==i:
                stk[-1][1]+=1
                if(stk[-1][1]==k):
                    stk.pop()
            else:
                stk.append([i,1])
        
        news=''
        for i in stk:
            news+=i[0]*i[1]
        return news