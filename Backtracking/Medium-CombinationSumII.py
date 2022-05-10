class Solution:
    
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        def backtrack(li):
            if(sum(li)==n and len(li)==k):
                res.append(li)
                return
            if(sum(li)>n or len(li)>k):
                return
            else:
                if(len(li)!=0):
                    for i in range(li[-1]+1,10):
                        backtrack(li+[i])
                else:
                    for i in range(1,10):
                        backtrack(li+[i])
        
        backtrack([])
        return(res)