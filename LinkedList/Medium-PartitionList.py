# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if (not head):
            return
        li=[]
        
        begin=head
        while(head):
            if(head.val<x):
                li.append(head.val)
                head=head.next
            else:
                break
        
        temph=head
        prev=head
        if(not head):
            return begin
        head=head.next
        while(head):
            while(head and head.val<x):
                li.append(head.val)
                head=head.next
            
            prev.next=head
            prev=prev.next
            if(head):
                head=head.next
        
        newh=ListNode(0)
        sa=newh
        while(li):
            newh.next=ListNode(li.pop(0))
            newh=newh.next
        newh.next=temph
            
        return sa.next