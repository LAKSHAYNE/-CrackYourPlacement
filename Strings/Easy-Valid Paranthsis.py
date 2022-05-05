class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        stack.append(s[0])
        for i in range(1,len(s)):
            if(stack):
                if((s[i]==')'and stack[-1]=='(') or (s[i]=='}'and stack[-1]=='{')or(s[i]==']'and stack[-1]=='[')):
                    stack.pop()
                else: 
                    stack.append(s[i])
            else: 
                stack.append(s[i])
        if(not stack):
            return True
        return False