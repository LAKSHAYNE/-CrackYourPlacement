# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(not root):
            return 
        count=0
        st=[]
        q=[root]
        ans=[[root.val]]
        while(q):
            n=len(q)
            for _ in range(n):
                node=q.pop(0)
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
            if(count%2!=0):
                for i in q:
                    st.append(i.val)
            else:
                for i in q[::-1]:
                    st.append(i.val)
            count+=1
            ans.append(st)
            st=[]
        return ans[:-1]