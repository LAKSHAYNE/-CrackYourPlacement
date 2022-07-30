# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if(not head):
            return 
        #findiing the mid
        slow,fast=head,head
        
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        
        #rev second half
        prev,curr=None,slow.next
        while(curr):
            nextt=curr.next
            curr.next=prev
            prev=curr
            curr=nextt
            
        slow.next=None
        head1,head2=head,prev
        #merge
        while(head2):
            nextt=head1.next
            head1.next=head2
            head1=head2
            head2=nextt