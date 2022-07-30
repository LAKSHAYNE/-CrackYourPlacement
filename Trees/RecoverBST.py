# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        li=[]
        temp=root
        def inor(root,li):
            if(root):
                inor(root.left,li)
                li.append(root.val)
                inor(root.right,li)
        
        def seti(root,li):
            if(root):
                seti(root.left,li)
                root.val=li.pop(0)
                seti(root.right,li)
        
        inor(root,li)
        li.sort()
        seti(temp,li)