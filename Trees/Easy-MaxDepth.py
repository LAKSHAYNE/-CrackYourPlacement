# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans=0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root,count):
            if(root):
                self.ans=max(self.ans,count)
                dfs(root.left,count+1)
                dfs(root.right,count+1)
        dfs(root,1)
        return self.ans