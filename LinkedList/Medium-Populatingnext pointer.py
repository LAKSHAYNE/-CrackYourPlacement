"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        li=[root]
        q=[root]
        while(q):
            node=q.pop(0)
            if(node):
                q.append(node.left)
                q.append(node.right)
                if(node.left):
                    li.append(node.left)
                if(node.right):
                    li.append(node.right)
        i=0
        start=0
        end=0
        #print('len',len(li))
        while((end+2**i)<len(li)):
            #print('in')
            if(i==0):
                li[0].next=None
                end=0
            else:
                start=end+1
                end=end+2**i
                #print(start,end)
                for k in range(start,end):
                    li[k].next=li[k+1]
                li[end].next=None
            i+=1
            #print('end',end,2**i,i,end+2**i)
        return root
            