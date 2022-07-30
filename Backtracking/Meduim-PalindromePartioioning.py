class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def f(curr,ind,li,ans):
            if(ind==len(s)):
                ans.append([*li])
            for i in range(ind,len(s)):
                c=s[ind:i+1]
                if(c and c==c[::-1]):
                    li.append(c)
                    f(curr,i+1,li,ans)
                    li.pop()
        ans=[]
        f('',0,[],ans)
        return ans
                    