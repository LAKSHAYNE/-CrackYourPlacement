# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans=[]
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(root,li):
            if(root):
                if (root.left==None and root.right==None):
                    self.ans.append(li+[str(root.val)])
                    return
                dfs(root.left,li+[str(root.val)])
                dfs(root.right,li+[str(root.val)])
        
        dfs(root,[])
        for i in range(len(self.ans)):
            self.ans[i]='->'.join(self.ans[i])
        return(self.ans)