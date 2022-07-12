# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.path=0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node,target):
            if(not node):
                return 
            dfs2(node,target)
            dfs(node.left,target)
            dfs(node.right,target)
        
        def dfs2(node,target):
            if(not node):
                return 
            if(node.val==target):
                self.path+=1
            
            dfs2(node.left,target-node.val)
            dfs2(node.right,target-node.val)
                
        dfs(root,targetSum)
        return self.path