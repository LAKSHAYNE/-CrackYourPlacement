#User function Template for python3


class Solution:
    def maxArea(self,M, n, m):
        # code here
        def maxar(heights):
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
        
        maxi=max(0,maxar(list(M[0])))    
        for i in range(1,n):
            for j in range(m):
                if(M[i][j]!=0):
                    M[i][j]=M[i-1][j]+M[i][j]
            maxi=max(maxi,maxar(list(M[i])))
        return maxi
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3



# Driver Code 
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        R,C = map(int, input().strip().split())
        A = []
        for i in range(R):
            line = [int(x) for x in input().strip().split()]
            A.append(line)
        print(Solution().maxArea(A, R, C)) 
	
# This code is contributed 
# by SHUBHAMSINGH10 

# } Driver Code Ends