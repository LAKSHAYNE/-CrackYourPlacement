# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count=0
        temp=head
        while(temp):
            count+=1
            temp=temp.next
        if(count==1):
            return head
        count=count//2+1
        flag=0
        while(head):
            flag+=1
            if(flag==count):
                return head
            head=head.next
        
        