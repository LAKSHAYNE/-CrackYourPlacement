# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans=[]
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def helper(start,end):
            a=[]
            if(start>end):
                return [None]
            for i in range(start,end+1):
                left=helper(start,i-1)
                right=helper(i+1,end)
                for l in left:
                    for r in right:
                        root=TreeNode(i)
                        root.left=l
                        root.right=r
                        a.append(root)
            return a
        
        return helper(1,n)