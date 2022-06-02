# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.a=[]
    def inorderTraversal(self, rooti: Optional[TreeNode]) -> List[int]:
        def inorderTraversa(root):
            if(not root):
                return None
            else:
                inorderTraversa(root.left)
                self.a.append(root.val)
                inorderTraversa(root.right)
        inorderTraversa(rooti)
        return self.a