class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res= list(str(bin(int(a,2)+int(b,2))))
        if('1' not in res):
            return '0'
        res=res[2:]
        i=0
        while(True):
            if(res[i]=='1'):
                break
            else:
                res.pop(0)
                continue
            i+=1
        return ''.join(res)
                
                