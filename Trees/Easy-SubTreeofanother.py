# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def trav(rootr):
            q=[rootr]
            ans=[]
            while(q):
                node=q.pop(0)
                if(node):
                    ans.append(node.val)
                else:
                    ans.append(None)
                if(node):
                    q.append(node.left)
                    q.append(node.right)
            return ans
        
        subans=trav(subRoot)
        q=[root]
        while(q):
            node=q.pop(0)
            if(node):
                if(node.val==subRoot.val):
                    rootans=trav(node)
                    if(rootans==subans):
                        return True
                q.append(node.left)
                q.append(node.right)
        return False
        