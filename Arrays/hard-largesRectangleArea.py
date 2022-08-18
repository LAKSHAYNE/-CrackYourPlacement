class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
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
        