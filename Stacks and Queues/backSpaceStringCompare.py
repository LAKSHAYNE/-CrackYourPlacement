class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sn=''
        for i in (s):
            if(i=='#'):
                sn=sn[:-1]
            else:
                sn+=i
        
        tn=''
        for i in (t):
            if(i=='#'):
                tn=tn[:-1]
            else:
                tn+=i
        #print(sn,tn)
        return sn==tn
        