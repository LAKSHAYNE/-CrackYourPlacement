# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def trav(root):
            if(root):
                ans=[[root.val]]
                q=[root]
                while(q):
                    count=(len(q))
                    li=[]
                    for _ in range(count):
                        node=q.pop(0)
                        if(node.left):
                            q.append(node.left)
                            li.append(node.left.val)
                        if(node.right):
                            q.append(node.right)
                            li.append(node.right.val)
                    if(li):
                        ans.append(li)
                return ans
        return trav(root)