# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q=[root]
        while(q):
            count=len(q)
            ans=[]
            ansr=[]
            for _ in range(count):
                node=q.pop(0)
                if(node):
                    ans.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                else:
                    ans.append(None)
                
                
            if(ans!=ans[::-1]):
                return False
        return True