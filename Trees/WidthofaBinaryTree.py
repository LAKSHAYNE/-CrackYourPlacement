class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # If parent is i index
        # Left child is => 2 * i + 1
        # Right child is => 2 * i + 2
        
        # add (root, index)
        q = collections.deque([(root, 0)])
        maxWidth = 0
        while q:
            left = right = 0
            for i in range(len(q)):
                node, index = q.popleft()
                if left is 0:
                    left = index
                else:
                    right = index
                if node:
                    if node.left:
                        q.append((node.left, 2 * index + 1))
                    if node.right:
                        q.append((node.right, 2 * index + 2))
            maxWidth = max(maxWidth, right - left +1)
        return maxWidth