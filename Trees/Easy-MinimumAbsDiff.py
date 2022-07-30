# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans=[]
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def trav(root):
            if(root):
                self.ans.append(root.val)
                trav(root.left)
                trav(root.right)
        trav(root)
        self.ans.sort()
        print(self.ans)
        for i in range(len(self.ans)-1):
            ans=min(ans,abs(self.ans[i]-self.ans[i+1]))
        return ans