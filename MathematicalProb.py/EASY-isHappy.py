class Solution:
    def isHappy(self, n: int) -> bool:
        while(True):
            sumi=0
            n=str(n)
            for i in n:
                sumi+=int(i)**2
            sumi=str(sumi)
            if(len(sumi)==1):
                if(sumi=='1' or sumi=='7'):
                    return True
                else:
                    return False
            n=sumi