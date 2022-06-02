# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        rootl=0
        rootr=0
        temp=root
        while(temp):
            temp=temp.right
            if(temp!=None):
                rootr+=1
        temp=root
        while(temp):
            temp=temp.left
            if(temp!=None):
                rootl+=1
        print(rootl,rootr)
        return rootl+rootr