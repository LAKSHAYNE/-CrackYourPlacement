# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        q=[root]
        ans=0
        while(q):
            node=q.pop(0)
            if(node):
                if(low<=node.val<=high):
                    ans+=node.val
                    q.append(node.left)
                    q.append(node.right)
                if(node.val<low):
                    q.append(node.right)
                if(node.val>high):
                    q.append(node.left)
        return ans