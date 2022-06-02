# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def trav(root):
            li=[]
            qu=[root]
            while(qu):
                node=qu.pop(0)
                if(node):
                    li.append(node.val)
                else:
                    li.append(None)
                if(node):
                    qu.append(node.right)
                    qu.append(node.left)
            return li
        
        return trav(q)==trav(p)
            