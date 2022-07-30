# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> Optional[TreeNode]:
        st=[pre[0]]
        visi=set()
        visi.add(pre[0])
        ino=[pre[0]]
        while(st):
            node=st.pop(0)
            inde=pre.index(node)
            if(inde+1<len(pre) and pre[inde+1] not in visi):
                ino.append(pre[inde+1])
                st.append(pre[inde+1])
                visi.add(pre[inde+1])
            else:
                ino.append('null')
            inde=post.index(node)
            if(inde-1>=0 and post[inde-1] not in visi):
                ino.append(post[inde-1])
                st.append(post[inde-1])
                visi.add(post[inde-1])
            else:
                ino.append('null')
        i=len(ino)-1
        while(ino):
            if(ino[i]=='null'):
                ino.pop()
                i-=1
            else:
                break
                
                
        root=TreeNode(ino.pop(0))
        q=[root]
        while(ino):
            node=q.pop(0)
            if(ino):
                node.left=TreeNode(ino.pop(0))
            if(ino):
                node.right=TreeNode(ino.pop(0))
            q.append(node.left)
            q.append(node.right)
        
        return root
            
        
            