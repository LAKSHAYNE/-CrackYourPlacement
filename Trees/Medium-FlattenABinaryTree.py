# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if(not root):
            return root
        def dfs(node):
            if(node):
                if(not node.left and not node.right):
                    return node
                a=dfs(node.left)
                b=dfs(node.right)
                if(a and b):
                    temp=a
                    while(a.right!=None):
                        a=a.right
                    a.right=b
                    node.right=temp
                    node.left=None
                if(a and not b):
                    print(a.val,node)
                    node.right=a
                    node.left=None
                return node
                    
        dfs(root)