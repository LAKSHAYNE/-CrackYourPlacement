class Solution:
    def simplifyPath(self, path: str) -> str:
        li=path.split('/')
        s=[]
        for i in li:
            if(i=='..' and s):
                a=s.pop()
                while(a=='.'):
                    a=s.pop()
            elif(i and i!='..' and i!='.'):
                s.append(i)
        if(s and s[-1]=='.' ):
            s.pop()
        return '/'+'/'.join(s) if(s) else '/'
        