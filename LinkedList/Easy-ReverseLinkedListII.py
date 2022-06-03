# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cou=0
        temp=head
        li=[]
        while(head):
            cou+=1
            if(cou>=left and cou<=right):
                li.append(head.val)
            head=head.next
        cou=0
        head=temp
        while(head):
            cou+=1
            if(cou>=left and cou<=right):
                head.val=(li.pop())
            head=head.next
        return temp
            