# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sumi=[]
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if(not root):
            return
        def dfs(root,count):
            if(root):
                if(root.left==None and root.right==None):
                    self.sumi.append(count)
                dfs(root.left,count+root.left.val if(root.left) else count)
                dfs(root.right,count+root.right.val if(root.right) else count)
        dfs(root,root.val)
        return targetSum in self.sumi