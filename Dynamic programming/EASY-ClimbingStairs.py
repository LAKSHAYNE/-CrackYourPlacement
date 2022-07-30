class Solution:
    ##because if we carefully look into it we can see that it is froming fibonacci series
    def climbStairs(self, n: int) -> int:
        one=1
        two=1
        for i in range(2,n+1):
            temp=two
            two+=one
            one=temp
        return two