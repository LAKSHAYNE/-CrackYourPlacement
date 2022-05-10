class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def backtrack(li):
            if(len(li)==k):
                res.append(li)
            else:
                if(len(li)!=0):
                    for i in range(li[-1]+1,n+1):
                        backtrack(li+[i])
                else:
                    for i in range(1,n+1):
                        backtrack([i])
                        
        backtrack([])
        return res