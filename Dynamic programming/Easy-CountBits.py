class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res = [0] * (n+1)
        
        for i in range(1,len(res)):
            if i%2 != 0:
                res[i] = 1 + res[i-1]
            else:
                res[i] = res[i//2]
        return res
        