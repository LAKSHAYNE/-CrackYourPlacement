# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.i=0
        self.ans=0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def small(rooet):
            if(rooet):
                small(rooet.left)
                self.i+=1
                if(self.i==k):
                    self.ans=rooet.val
                    return
                small(rooet.right)
        small(root)
        return self.ans
            
                