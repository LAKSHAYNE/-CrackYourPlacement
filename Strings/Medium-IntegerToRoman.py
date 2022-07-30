class Solution:
    def __init__(self):
        self.symbols=[('M',1000),('CM',900),('D',500),('CD',400),('C',100),('XC',90),('L',50),('XL',40),('X',10),('IX',9),('V',5),('IV',4),('I',1)]
    def intToRoman(self, num: int) -> str:
        if(num==0):
            return ''
        fac=0
        ind=0
        for index,symbol in enumerate(self.symbols):
            if(num%symbol[1]==num):
                continue
            elif(num%symbol[1]<num):
                fac=num//symbol[1]
                ind=index
                break
        return self.symbols[ind][0]*fac+self.intToRoman(num-self.symbols[ind][1]*fac)