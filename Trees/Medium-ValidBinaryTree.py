# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root,gre,less):
            if(not root):
                return True
            if(root):
                if((gre>=root.val) or (less<=root.val)):
                    return False
            return (dfs(root.right,max(root.val,gre),less) and dfs(root.left,gre,min(root.val,less)))
                

        return dfs(root,float('-inf'),float('inf'))