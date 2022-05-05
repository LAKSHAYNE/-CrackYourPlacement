# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.st=[]
        def ine(rootn):
            if(rootn):
                ine(rootn.left)
                self.st.append(rootn.val)
                ine(rootn.right)
        ine(root)

    def next(self) -> int:
        return self.st.pop(0)

    def hasNext(self) -> bool:
        return True if(self.st) else False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()