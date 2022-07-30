# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans=0
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def trav(root):
            if(root):
                if(root.left and root.left.right==None and root.left.left==None):
                    self.ans+=root.left.val
                trav(root.left)
                trav(root.right)
        trav(root)
        return self.ans