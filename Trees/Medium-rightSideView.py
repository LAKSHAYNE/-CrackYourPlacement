# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


###do this ny simple ;evel order traversal
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q=[root]
        if(not root):
            return
        if(root):
            ans=[root.val]
        
        while(q):
            temp=[]
            for node in q:
                if(node.left):
                    temp.append(node.left)
                if(node.right):
                    temp.append(node.right)
            #print(temp)
            if(temp):
                ans.append(temp[-1].val)
            q=temp
        return ans
            