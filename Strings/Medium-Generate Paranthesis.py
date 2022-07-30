class Solution:
    def __init__(self):
        self.li=[]
    def generateParenthesis(self, n: int) -> List[str]:
        def gen(target,curr,close,ope):
            if(ope<close):
                return
            if(ope==target and close==target):
                return
            else:
                if(ope==target):
                    self.li.append(curr+')')
                    gen(target,curr+')',close+1,ope)
                else:
                    self.li.append(curr+')')
                    self.li.append(curr+'(')
                    gen(target,curr+')',close+1,ope)
                    gen(target,curr+'(',close,ope+1)
        gen(n,'',0,0) 
        a=[]
        for i in self.li:
            if len(i)==n*2:
                a.append(i)
        return a