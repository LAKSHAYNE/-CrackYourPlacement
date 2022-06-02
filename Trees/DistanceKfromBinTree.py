# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj=collections.defaultdict(list)#doesn,t raise keyerror
        def toGraph(parent,child):
            if(parent and child):
                adj[parent.val].append(child.val)
                adj[child.val].append(parent.val)
            
            if(child.left):
                toGraph(child,child.left)
            if(child.right):
                toGraph(child,child.right)
        
        toGraph(None,root)
        visi=set()
        visi.add(target.val)
        neighbour=[target.val]
        for i in range(k):
            new=[]
            while(neighbour):
                node=neighbour.pop(0)
                for it in adj[node]:
                    if(it not in visi):
                        visi.add(it)
                        new.append(it)
            neighbour=new.copy()
        
        return neighbour
                