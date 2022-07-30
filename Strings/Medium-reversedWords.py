class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(' ')
        li=[]
        for i in reversed(s):
            if(i):
                li.append(i)
        return ' '.join(li)