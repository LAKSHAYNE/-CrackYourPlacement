# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        root=head
        while(head):
            head=head.next
            count+=1
        head=root
        if(count==n):
            return head.next
        ch=count-n
        prev=head
        #print(ch,n,count)
        for i in range(1,count+1):
            #print(head.val)
            if(not i==ch):
                #print(prev.val)
                prev.next=head.next
                prev=prev.next
            head=head.next
        return root