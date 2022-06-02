# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def trav(root,p,q):
            if root is None:
                return None

            if root.val > max(p.val, q.val):
                return trav(root.left, p, q)

            elif root.val < min(p.val, q.val):
                return trav(root.right, p, q)

            
            return root
        return trav(root,p,q)