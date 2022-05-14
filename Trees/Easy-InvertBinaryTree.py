# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def trav(roo):
            q=[roo]
            while(q):
                r=q.pop(0)
                if(r):
                    r.left,r.right=r.right,r.left
                    q.append(r.left)
                    q.append(r.right)
            
            
        trav(root)
        return root