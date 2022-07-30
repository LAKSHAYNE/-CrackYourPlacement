class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def maxrec(heights):
            st=[]
            ans=0
            heights.append(0)
            for i in range(len(heights)):
                while(st and heights[i]<heights[st[-1]]):
                    height=heights[st[-1]]
                    st.pop()
                    if(st):
                        width=i-st[-1]-1
                    else:
                        width=i
                    ans=max(ans,height*width)
                st.append(i)
            return ans
        
        prev=[0]*len(matrix[0])
        ans=0
        def check(a,b):
            if(b==0):
                return 0
            else:
                return a+b
        for i in matrix:
            i=list(map(int,i))
            prev=list(map(check,prev,i))
            ans=max(ans,maxrec(prev))
        return ans